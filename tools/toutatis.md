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

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| phone (`p`) | `p:+15551234567` | `--phone +15551234567` |

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run toutatis -- --phone +15551234567
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run toutatis p:+15551234567
```

Results are saved to `./results/toutatis/<target>/`.
