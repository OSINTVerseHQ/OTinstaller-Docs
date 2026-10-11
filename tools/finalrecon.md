# Finalrecon

All In One Web Recon.

## Source

- Repository: https://github.com/thewhiteh4t/FinalRecon
- License: MIT

## Install

```bash
otinstaller install finalrecon
```

otinstaller clones `https://github.com/thewhiteh4t/FinalRecon.git` at ref `b5db3a46921195bec643065c560e19741852957c` into a dedicated virtualenv, then installs the dependencies listed in `requirements.txt`.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| url (`url`) | `url:https://example.com` | `--url https://example.com` |

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run finalrecon -- --url https://example.com
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run finalrecon url:https://example.com
```

Results are saved to `./results/finalrecon/<target>/`.
