# Fierce

A DNS reconnaissance tool for locating non-contiguous IP space.

## Source

- Repository: https://github.com/mschwager/fierce
- License: GPL-3.0

## Install

```bash
otinstaller install fierce
```

otinstaller installs the pip package `fierce` pinned to version `1.6.0` in a dedicated virtualenv.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| domain (`d`) | `d:example.com` | `--domain example.com` |

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run fierce -- --domain example.com
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run fierce d:example.com
```

Results are saved to `./results/fierce/<target>/`.
