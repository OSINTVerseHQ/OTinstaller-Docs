# Onionsearch

OnionSearch is a script that scrapes urls on different.

## Source

- Repository: https://github.com/megadose/OnionSearch
- License: GPL-3.0

## Install

```bash
otinstaller install onionsearch
```

otinstaller installs the pip package `onionsearch` pinned to version `1.3` in a dedicated virtualenv.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| query (`q`) | `q:example` | `example` (positional) |

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run onionsearch -- example
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run onionsearch q:example
```

Results are saved to `./results/onionsearch/<target>/`.
