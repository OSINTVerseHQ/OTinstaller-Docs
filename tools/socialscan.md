# Socialscan

Python library for accurately querying username and email usage on online platforms.

## Source

- Repository: https://github.com/iojw/socialscan
- License: MPL-2.0

## Install

```bash
otinstaller install socialscan
```

otinstaller installs the pip package `socialscan` pinned to version `2.0.1` in a dedicated virtualenv.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| query (`q`) | `q:example` | `example` (positional) |

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run socialscan -- example
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run socialscan q:example
```

Results are saved to `./results/socialscan/<target>/`.
