# Bbot

The recursive internet scanner for hackers.

## Source

- Repository: https://github.com/blacklanternsecurity/bbot
- License: AGPL-3.0

## Install

```bash
otinstaller install bbot
```

otinstaller installs the pip package `bbot` pinned to version `3.0.2` in a dedicated virtualenv.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| domain (`d`) | `d:example.com` | `--domain example.com` |
| username (`u`) | `u:exampleuser` | `--username exampleuser` |

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run bbot -- --domain example.com --username exampleuser
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run bbot d:example.com u:exampleuser
```

Results are saved to `./results/bbot/<target>/`.
