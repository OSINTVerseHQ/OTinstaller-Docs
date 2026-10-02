# Nexfil

OSINT tool for finding profiles by username.

## Source

- Repository: https://github.com/thewhiteh4t/nexfil
- License: MIT

## Install

```bash
otinstaller install nexfil
```

otinstaller installs the pip package `nexfil` pinned to version `1.0.6` in a dedicated virtualenv.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| username (`u`) | `u:exampleuser` | `--username exampleuser` |

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run nexfil -- --username exampleuser
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run nexfil u:exampleuser
```

Results are saved to `./results/nexfil/<target>/`.
