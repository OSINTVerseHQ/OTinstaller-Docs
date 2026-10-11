# Toutatis

Toutatis is a tool that allows you to extract information from instagrams accounts such as e-mails, phone numbers and more.

## Source

- Repository: https://github.com/megadose/toutatis
- License: GPL-3.0

## Install

```bash
otinstaller install toutatis
```

otinstaller installs the pip package `toutatis` pinned to version `1.31` in a dedicated virtualenv.

## Credentials

No API keys needed.

This tool still needs manual configuration before the first run.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| username (`u`) | `u:exampleuser` | `--username exampleuser` |

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run toutatis -- --username exampleuser
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run toutatis u:exampleuser
```

Results are saved to `./results/toutatis/<target>/`.
