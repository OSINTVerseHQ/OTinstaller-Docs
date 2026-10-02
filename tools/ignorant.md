# Ignorant

ignorant allows you to check if a phone number is used on different sites like snapchat, instagram.

## Source

- Repository: https://github.com/megadose/ignorant
- License: GPL-3.0

## Install

```bash
otinstaller install ignorant
```

otinstaller installs the pip package `ignorant` pinned to version `1.2` in a dedicated virtualenv.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| phone (`p`) | `p:+15551234567` | `--phone +15551234567` |

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run ignorant -- --phone +15551234567
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run ignorant p:+15551234567
```

Results are saved to `./results/ignorant/<target>/`.
