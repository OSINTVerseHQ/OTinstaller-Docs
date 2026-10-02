# Getting started

## Requirements

A Linux machine with Python 3.10 or newer, git, and the `venv` module. On Debian,
Ubuntu and Kali, install them with:

```bash
sudo apt install python3-venv git
```

Some managed tools do not support Python 3.13 or newer yet. The test matrix
covers Python 3.10 to 3.12.

## Install otinstaller

otinstaller is not published to PyPI yet, so install it from a checkout of the
otinstaller repository:

```bash
cd OTinstaller
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

To get the `otinstaller` and `ot` commands on your PATH without activating a
virtualenv, use `pipx install .` from the checkout instead.

Check the machine:

```bash
otinstaller doctor
```

## Initialize

```bash
otinstaller init
```

This shows the responsible use notice and creates `~/.otinstaller/`, the home
directory for tools, logs, and the API key file `~/.otinstaller/.env` (kept at
permissions 600). Use `otinstaller init --yes` to accept the notice without a
prompt. Install and run commands refuse to work until the notice is accepted.

## Find a tool

```bash
otinstaller list
otinstaller search sherlock
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

Typed inputs are an alternative. otinstaller maps each one to the flag the tool
expects:

```bash
otinstaller run sherlock u:exampleuser
```

otinstaller prints `ok` or `failed` per tool and saves the output to
`./results/<tool>/<target>/` with a `.meta.json` sidecar file.

Run several tools at once by listing more names, or every installed tool that
accepts the input with `--all`:

```bash
otinstaller run sherlock maigret u:exampleuser
```

## API keys

Some tools need API keys. Add them to `~/.otinstaller/.env`, one `KEY=value` per
line, then check what is missing:

```bash
otinstaller keys check
```

Each tool only receives the keys declared in its registry entry.

## Updates and removal

```bash
otinstaller check-updates
otinstaller update --all
otinstaller remove sherlock
```

If a run is interrupted, `otinstaller resume` picks up where it stopped and skips
jobs that already finished.
