# Getting started

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
