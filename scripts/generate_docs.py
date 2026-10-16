#!/usr/bin/env python3
"""Generate the GitBook markdown pages from an otinstaller data directory.

Usage:
    python3 scripts/generate_docs.py --data-dir /path/to/otinstaller/src/otinstaller/data

Requires PyYAML. Writes README.md, getting-started.md, SUMMARY.md and one
page per registry tool under tools/. Existing pages under tools/ are removed
first so tools dropped from the registry disappear on regeneration.

A hand-written scripts/notes/<tool>.md, if there is one, is added to the end of
that tool's page, for usage the registry can't describe.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

import yaml

PREFIX_LABELS = {
    "u": "username",
    "e": "email",
    "p": "phone",
    "d": "domain",
    "url": "url",
    "q": "query",
    "geo": "coordinates",
    "tg": "telegram channel",
    "lat": "latitude",
    "lng": "longitude",
}

PREFIX_VALUES = {
    "u": "exampleuser",
    "e": "example@example.com",
    "p": "+15551234567",
    "d": "example.com",
    "url": "https://example.com",
    "q": "example",
    "geo": "40.7128,-74.0060",
    "tg": "examplechannel",
    "lat": "40.7128",
    "lng": "-74.0060",
}

SAFE_NAME = re.compile(r"[a-z0-9][a-z0-9-]*\Z")


def load_tools(data_dir: Path) -> list[dict]:
    registry = yaml.safe_load((data_dir / "registry.yaml").read_text())
    tools = registry.get("tools") or []
    if not tools:
        sys.exit("error: no tools found in registry.yaml")
    for tool in tools:
        if not SAFE_NAME.fullmatch(tool["name"]):
            sys.exit(f"error: unsafe tool name in registry: {tool['name']!r}")
    return tools


def install_sentence(tool: dict) -> str:
    install = tool["install"]
    if install.get("method") == "pip":
        line = f"otinstaller installs the pip package `{install['package']}`"
        if install.get("version"):
            line += f" pinned to version `{install['version']}`"
        return line + " in a dedicated virtualenv." + extras_sentence(install)
    line = f"otinstaller clones `{install['url']}`"
    if install.get("ref"):
        line += f" at ref `{install['ref']}`"
    line += " into a dedicated virtualenv, then "
    parts = []
    if install.get("requirements"):
        parts.append(f"installs the dependencies listed in `{install['requirements']}`")
    if install.get("as_package"):
        parts.append("installs the clone itself as a package")
    if not parts:
        parts.append("installs nothing further (the tool runs from the clone)")
    return line + " and ".join(parts) + "." + extras_sentence(install)


def extras_sentence(install: dict) -> str:
    """Extra packages and Playwright browsers installed after the tool itself."""
    text = ""
    names = [f"`{p}`" for p in install.get("extra_packages") or []]
    if names:
        listed = names[0] if len(names) == 1 else ", ".join(names[:-1]) + " and " + names[-1]
        text += f" It also installs {listed}."
    browsers = install.get("playwright_browsers") or []
    if browsers:
        browser_names = ", ".join(b.capitalize() for b in browsers)
        text += (
            f" Then Playwright downloads {browser_names} (the headless shell) into the "
            "tool's own folder, so `otinstaller remove` deletes it too."
        )
    return text


def credentials_section(tool: dict) -> str:
    required = tool.get("api_keys", {}).get("required") or []
    optional = tool.get("api_keys", {}).get("optional") or []
    lines = []
    if required:
        lines.append("Required keys: " + ", ".join(f"`{k}`" for k in required) + ".")
    if optional:
        lines.append("Optional keys: " + ", ".join(f"`{k}`" for k in optional) + ".")
    if required or optional:
        lines.append("")
        lines.append(
            "Keys are stored in `~/.otinstaller/.env`, one `KEY=value` per line. "
            "This tool only receives the keys listed above."
        )
        if tool.get("needs_config"):
            lines.append("")
            lines.append(
                "After install, otinstaller warns that this tool requires "
                "configuration: set these keys before the first run."
            )
    else:
        lines.append("No API keys needed.")
        if tool.get("needs_config"):
            lines.append("")
            lines.append(
                "This tool still needs manual configuration before the first run."
            )
    return "\n".join(lines)


def input_rows(tool: dict) -> list[tuple[str, str, str, str]]:
    rows = []
    for prefix, flag in (tool.get("input_types") or {}).items():
        label = PREFIX_LABELS.get(prefix, prefix)
        value = PREFIX_VALUES.get(prefix, "value")
        typed = f"{prefix}:{value}"
        if flag:
            result = f"`{flag} {value}`"
        else:
            result = f"`{value}` (positional)"
        rows.append((f"{label} (`{prefix}`)", typed, result))
    return rows


def passthrough_commands(tool: dict) -> list[str]:
    """One plain-argument command per input. default_args are left out: otinstaller adds them."""
    commands = []
    for prefix, flag in (tool.get("input_types") or {}).items():
        value = PREFIX_VALUES.get(prefix, "value")
        args = f"{flag} {value}" if flag else value
        commands.append(f"otinstaller run {tool['name']} -- {args}")
    return commands


def typed_commands(tool: dict) -> list[str]:
    """One typed-input command per input (a tool takes one input per run)."""
    return [
        f"otinstaller run {tool['name']} {prefix}:{PREFIX_VALUES.get(prefix, 'value')}"
        for prefix in (tool.get("input_types") or {})
    ]


def notes_section(tool: dict, notes_dir: Path | None) -> list[str]:
    """Hand-written notes for a tool (scripts/notes/<name>.md), added to the end of its page."""
    if notes_dir is None:
        return []
    path = notes_dir / f"{tool['name']}.md"
    if not path.is_file():
        return []
    return [path.read_text().rstrip("\n"), ""]


def tool_page(tool: dict, data_dir: Path, notes_dir: Path | None = None) -> str:
    lines = [f"# {tool['display_name']}", "", tool["description"], ""]
    lines += ["## Source", ""]
    lines.append(f"- Repository: https://github.com/{tool['repo']}")
    lines.append(f"- License: {tool.get('license') or 'not stated'}")
    lines += ["", "## Install", "", "```bash", f"otinstaller install {tool['name']}", "```", ""]
    lines.append(install_sentence(tool))
    lines += ["", "## Credentials", "", credentials_section(tool)]
    if tool.get("long_running"):
        lines += [
            "",
            "This tool monitors its target continuously and does not exit on its own. "
            "It is never started by `otinstaller run --all` or `otinstaller auto`; "
            "run it by name and stop it with Ctrl+C.",
        ]

    rows = input_rows(tool)
    if rows:
        lines += [
            "",
            "## Input types",
            "",
            "| Input | Typed input | Tool arguments |",
            "| --- | --- | --- |",
        ]
        for label, typed, result in rows:
            lines.append(f"| {label} | `{typed}` | {result} |")
        defaults = tool.get("default_args") or []
        if defaults:
            lines += [
                "",
                "otinstaller always adds these arguments first: "
                + "`" + " ".join(str(a) for a in defaults) + "`.",
            ]

    example = tool.get("example")
    if example:
        example_path = data_dir / example
        if example_path.is_file():
            lines += [
                "",
                "## Example output",
                "",
                "Illustrative output showing the general shape of a run. Real output "
                "depends on the tool version and the target.",
                "",
                "```text",
                example_path.read_text().rstrip("\n"),
                "```",
            ]

    lines += ["", "## Run", ""]
    if rows:
        lines += [
            "Plain arguments after `--` are passed to the tool unchanged:",
            "",
            "```bash",
            *passthrough_commands(tool),
            "```",
            "",
            "Typed inputs are mapped to this tool's flags:",
            "",
            "```bash",
            *typed_commands(tool),
            "```",
        ]
    else:
        lines += [
            "```bash",
            f"otinstaller run {tool['name']} -- --help",
            "```",
        ]
    lines += ["", f"Results are saved to `./results/{tool['name']}/<target>/`.", ""]
    lines += notes_section(tool, notes_dir)
    return "\n".join(lines)


def readme(count: int) -> str:
    return f"""# OTinstaller

![OTinstaller](images/otinstaller-banner.png)

OTinstaller is a command line tool manager for Linux. It installs, runs, updates
and removes open-source command line tools by name, each in its own virtualenv,
through one standard command interface. `ot` is a short alias for `otinstaller`.

You pick a tool by name. OTinstaller installs it, runs it against a target, and
saves the output under `./results/` with a metadata sidecar file. You do not learn
a different install method for every tool.

## Watch the launch video

{{% embed url="https://www.youtube.com/watch?v=_AfUGMFRaKA" %}}
90 seconds: install, typed inputs, auto-detect, parallel runs, results and more.
{{% endembed %}}

![Installing and running a tool](images/otinstaller-demo.png)

This site covers {count} tools. The tool list focuses on open-source intelligence
(OSINT) tooling and is rebuilt from the OTinstaller registry whenever the registry
changes.

## Contents

- [Getting started](getting-started.md): install OTinstaller, run `otinstaller
  init`, and run your first tool.
- Guides: [typed inputs](guides/typed-inputs.md), the
  [command reference](guides/commands.md), [results and resume](guides/results.md),
  [API keys](guides/api-keys.md) and [responsible use](guides/responsible-use.md).
- [FAQ](faq.md): Windows and macOS, root, data, uninstalling, legality.
- [Changelog](changelog.md): what changed in each release.
- Tools: one page per tool, grouped by what it searches, with source, install
  method, credentials, input flags, example output, and run commands.

## Links

- Source code: [github.com/OSINTVerseHQ/OTinstaller](https://github.com/OSINTVerseHQ/OTinstaller)
- Package: [pypi.org/project/otinstaller](https://pypi.org/project/otinstaller/)
- Report a bug or suggest a tool: [issues](https://github.com/OSINTVerseHQ/OTinstaller/issues)

## Team

- **Sushant Koul**, builder: [GitHub](https://github.com/Sushant-69x) ·
  [LinkedIn](https://www.linkedin.com/in/sushantkoul07)
- **Dheeraj Yadav**: [GitHub](https://github.com/dheerajydv19) ·
  [X](https://x.com/dheerajydv19)

Built by [OSINTverse](https://osintverse.com/).
"""


def getting_started() -> str:
    return """# Getting started

## Requirements

A Linux machine with Python 3.10 to 3.12, git, and the `venv` module. On Debian,
Ubuntu and Kali, install them with:

```bash
sudo apt install python3-venv git
```

## Install OTinstaller

OTinstaller is published on PyPI. The simplest install puts the `otinstaller` and
`ot` commands on your PATH:

```bash
pipx install otinstaller
```

Or install it into a virtualenv:

```bash
python3 -m venv ~/.otinstaller-venv
source ~/.otinstaller-venv/bin/activate
pip install otinstaller
```

Run `source ~/.otinstaller-venv/bin/activate` again in any new terminal.

### Systems with Python 3.13 or newer

Ubuntu 26.04 and other recent distributions ship Python 3.13 or 3.14. Some managed
tools do not support those versions yet, so use Python 3.12 through uv:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env
uv venv --python 3.12 ~/.otinstaller-venv
source ~/.otinstaller-venv/bin/activate
uv pip install otinstaller
```

Check the machine:

```bash
otinstaller doctor
```

## Initialize

```bash
otinstaller init
```

This shows the startup banner and the responsible use notice, and creates
`~/.otinstaller/`, the home directory for tools, logs, and the API key file
`~/.otinstaller/.env` (kept at permissions 600). Use `otinstaller init --yes` to
accept the notice without a prompt. Install and run commands refuse to work until
the notice is accepted.

The banner only appears in an interactive terminal. It is never printed with
`--json` or when output is piped, and `OTINSTALLER_NO_BANNER=1` turns it off.

## Find a tool

```bash
otinstaller list
otinstaller search username
otinstaller info sherlock
otinstaller example sherlock
```

## Install and run a tool

```bash
otinstaller install sherlock
```

Run it with plain arguments after `--`. Everything after `--` is passed to the
tool unchanged:

```bash
otinstaller run sherlock -- exampleuser
```

Typed inputs are an alternative. OTinstaller maps each one to the flag the tool
expects:

```bash
otinstaller run sherlock u:exampleuser
```

OTinstaller saves the output to `./results/<tool>/<target>/` with a `.meta.json`
sidecar file. Set `OTINSTALLER_RESULTS_DIR` to keep all results in one place.

Run several tools at once by listing more names, or every installed tool that
accepts the input with `--all`:

```bash
otinstaller run sherlock maigret u:exampleuser
otinstaller run --all u:exampleuser
```

`--all` skips tools that need API keys or a login unless `--include-credentialed`
is passed, and never starts tools that monitor a target continuously.

## API keys

Some tools need API keys. Add them to `~/.otinstaller/.env`, one `KEY=value` per
line, then check what is missing:

```bash
otinstaller keys check
```

From that file, each tool only receives the keys declared in its registry entry.
Tools also inherit your shell environment.

## Updates and removal

```bash
otinstaller check-updates
otinstaller update --all
otinstaller remove sherlock
```

If an install or run is cut off by a crash or a kill, `otinstaller resume` cleans
up and retries the install, or prints the command to rerun. Pressing Ctrl+C stops
cleanly, so there is nothing to resume.
"""


GUIDES = [
    ("guides/typed-inputs.md", "Typed inputs", ["Typed inputs", "Run every matching tool"]),
    ("guides/commands.md", "Command reference", ["Command reference"]),
    ("guides/results.md", "Results and resume", ["Results", "Resume"]),
    ("guides/api-keys.md", "API keys", ["API keys"]),
    ("guides/responsible-use.md", "Responsible use", ["Responsible use"]),
    ("faq.md", "FAQ", ["FAQ"]),
]
README_URL = "https://github.com/OSINTVerseHQ/OTinstaller"
ANCHORS = {"responsible-use": "guides/responsible-use.md", "faq": "faq.md",
           "typed-inputs": "guides/typed-inputs.md", "command-reference": "guides/commands.md",
           "results": "guides/results.md", "resume": "guides/results.md",
           "api-keys": "guides/api-keys.md", "run-every-matching-tool": "guides/typed-inputs.md"}
TOOL_GROUPS = [("username", "Username tools"), ("email", "Email tools"), ("phone", "Phone tools"),
               ("domain", "Domain tools"), ("ip", "IP address tools"), ("url", "URL tools"),
               ("name", "Name tools")]


def readme_sections(text: str) -> dict[str, str]:
    """Split the main README into its level-2 sections, keyed by heading."""
    sections: dict[str, str] = {}
    current = None
    for line in text.splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            sections[current] = ""
        elif current is not None:
            sections[current] += line + "\n"
    return {k: v.strip() + "\n" for k, v in sections.items()}


def fix_links(body: str, page: str) -> str:
    """Point README anchor links at the matching docs page, or back at the README."""
    import os
    import re

    def repl(m: re.Match) -> str:
        anchor = m.group(2)
        target = ANCHORS.get(anchor)
        if target:
            rel = os.path.relpath(target, os.path.dirname(page) or ".")
            return f"{m.group(1)}({rel})"
        return f"{m.group(1)}({README_URL}#{anchor})"

    return re.sub(r"(\[[^\]]*\])\(#([a-z0-9-]+)\)", repl, body)


def guide_pages(readme_text: str) -> dict[str, str]:
    sections = readme_sections(readme_text)
    pages = {}
    for path, title, heads in GUIDES:
        missing = [h for h in heads if h not in sections]
        if missing:
            sys.exit(f"error: README section not found: {missing}")
        if len(heads) == 1:
            body = sections[heads[0]]
        else:
            body = "\n".join(
                sections[h] if h == title else f"## {h}\n\n{sections[h]}" for h in heads
            )
        note = f"_This page mirrors the [OTinstaller README]({README_URL})._\n"
        pages[path] = f"# {title}\n\n{fix_links(body, path)}\n{note}"
    return pages


def summary(tools: list[dict]) -> str:
    lines = [
        "# Summary",
        "",
        "* [Introduction](README.md)",
        "* [Getting started](getting-started.md)",
        "* [FAQ](faq.md)",
        "* [Changelog](changelog.md)",
        "",
        "## Guides",
        "",
    ]
    lines += [f"* [{title}]({path})" for path, title, _ in GUIDES if path.startswith("guides/")]
    placed = set()
    for key, label in TOOL_GROUPS:
        group = sorted((t for t in tools if (t.get("accepts") or [None])[0] == key),
                       key=lambda t: t["display_name"].lower())
        if not group:
            continue
        lines += ["", f"## {label}", ""]
        for tool in group:
            lines.append(f"* [{tool['display_name']}](tools/{tool['name']}.md)")
            placed.add(tool["name"])
    rest = sorted((t for t in tools if t["name"] not in placed), key=lambda t: t["display_name"].lower())
    if rest:
        lines += ["", "## Other tools", ""]
        lines += [f"* [{t['display_name']}](tools/{t['name']}.md)" for t in rest]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--data-dir",
        type=Path,
        required=True,
        help="otinstaller src/otinstaller/data directory (registry.yaml and examples/)",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="output directory (default: repository root)",
    )
    parser.add_argument(
        "--readme",
        type=Path,
        help="OTinstaller README.md: guide pages and the FAQ are built from its sections",
    )
    parser.add_argument(
        "--changelog",
        type=Path,
        help="OTinstaller CHANGELOG.md: copied to changelog.md",
    )
    args = parser.parse_args()

    data_dir = args.data_dir
    if not (data_dir / "registry.yaml").is_file():
        sys.exit(f"error: {data_dir}/registry.yaml not found")

    tools = load_tools(data_dir)
    out: Path = args.out
    # Hand-written notes live next to this script, outside the published folders
    notes_dir = Path(__file__).resolve().parent / "notes"
    tools_dir = out / "tools"
    if tools_dir.exists():
        shutil.rmtree(tools_dir)
    tools_dir.mkdir(parents=True)

    (out / "README.md").write_text(readme(len(tools)))
    (out / "getting-started.md").write_text(getting_started())
    (out / "SUMMARY.md").write_text(summary(tools))
    for tool in tools:
        (tools_dir / f"{tool['name']}.md").write_text(tool_page(tool, data_dir, notes_dir))
    if args.readme:
        for path, text in guide_pages(args.readme.read_text()).items():
            (out / path).parent.mkdir(parents=True, exist_ok=True)
            (out / path).write_text(text)
    if args.changelog:
        (out / "changelog.md").write_text(args.changelog.read_text())

    print(f"wrote {len(tools)} tool pages to {tools_dir}")


if __name__ == "__main__":
    main()
