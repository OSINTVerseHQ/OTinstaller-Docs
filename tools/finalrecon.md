# Finalrecon

All In One Web Recon.

## Source

- Repository: https://github.com/thewhiteh4t/FinalRecon
- License: MIT

## Install

```bash
otinstaller install finalrecon
```

otinstaller clones `https://github.com/thewhiteh4t/FinalRecon.git` into a dedicated virtualenv, then installs the dependencies listed in `requirements.txt`.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| domain (`d`) | `d:example.com` | `--domain example.com` |

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run finalrecon -- --domain example.com
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run finalrecon d:example.com
```

Results are saved to `./results/finalrecon/<target>/`.
