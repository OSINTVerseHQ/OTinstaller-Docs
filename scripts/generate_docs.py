#!/usr/bin/env python3
"""Generate the GitBook markdown pages from an otinstaller data directory.

Usage:
    python3 scripts/generate_docs.py --data-dir /path/to/otinstaller/src/otinstaller/data

Requires PyYAML. Writes README.md, getting-started.md, SUMMARY.md and one
page per registry tool under tools/. Existing pages under tools/ are removed
first so tools dropped from the registry disappear on regeneration.
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
        return line + " in a dedicated virtualenv."
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
    return line + " and ".join(parts) + "."


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


def passthrough_args(tool: dict) -> str:
    args = [str(a) for a in (tool.get("default_args") or [])]
    for prefix, flag in (tool.get("input_types") or {}).items():
        value = PREFIX_VALUES.get(prefix, "value")
        if flag:
            args.extend([flag, value])
        else:
            args.append(value)
    return " ".join(args)


def typed_args(tool: dict) -> str:
    return " ".join(
        f"{prefix}:{PREFIX_VALUES.get(prefix, 'value')}"
        for prefix in (tool.get("input_types") or {})
    )


def tool_page(tool: dict, data_dir: Path) -> str:
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
            f"otinstaller run {tool['name']} -- {passthrough_args(tool)}",
            "```",
            "",
            "Typed inputs are mapped to this tool's flags:",
            "",
            "```bash",
            f"otinstaller run {tool['name']} {typed_args(tool)}",
            "```",
        ]
    else:
        lines += [
            "```bash",
            f"otinstaller run {tool['name']} -- --help",
            "```",
        ]
    lines += ["", f"Results are saved to `./results/{tool['name']}/<target>/`.", ""]
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

![Installing and running a tool](images/otinstaller-demo.png)

This site covers {count} tools. The tool list focuses on open-source intelligence
(OSINT) tooling and is rebuilt from the OTinstaller registry whenever the registry
changes.

## Contents

- [Getting started](getting-started.md): install OTinstaller, run `otinstaller
  init`, and run your first tool.
- [Changelog](changelog.md): what changed in each release.
- [Tools](SUMMARY.md): one page per tool with source, install method, credentials,
  input flags, example output, and run commands.

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


def summary(tools: list[dict]) -> str:
    lines = [
        "# Summary",
        "",
        "* [Introduction](README.md)",
        "* [Getting started](getting-started.md)",
        "* [Changelog](changelog.md)",
        "",
        "## Tools",
        "",
    ]
    for tool in tools:
        lines.append(f"* [{tool['display_name']}](tools/{tool['name']}.md)")
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
    args = parser.parse_args()

    data_dir = args.data_dir
    if not (data_dir / "registry.yaml").is_file():
        sys.exit(f"error: {data_dir}/registry.yaml not found")

    tools = load_tools(data_dir)
    out: Path = args.out
    tools_dir = out / "tools"
    if tools_dir.exists():
        shutil.rmtree(tools_dir)
    tools_dir.mkdir(parents=True)

    (out / "README.md").write_text(readme(len(tools)))
    (out / "getting-started.md").write_text(getting_started())
    (out / "SUMMARY.md").write_text(summary(tools))
    for tool in tools:
        (tools_dir / f"{tool['name']}.md").write_text(tool_page(tool, data_dir))

    print(f"wrote {len(tools)} tool pages to {tools_dir}")


if __name__ == "__main__":
    main()
