# Ivre

Network recon framework.

## Source

- Repository: https://github.com/ivre/ivre
- License: GPL-3.0

## Install

```bash
otinstaller install ivre
```

otinstaller installs the pip package `ivre` pinned to version `0.9.20` in a dedicated virtualenv.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| domain (`d`) | `d:example.com` | `--domain example.com` |

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run ivre -- --domain example.com
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run ivre d:example.com
```

Results are saved to `./results/ivre/<target>/`.
