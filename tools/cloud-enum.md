# Cloud Enum

Multi-cloud OSINT tool.

## Source

- Repository: https://github.com/initstring/cloud_enum
- License: MIT

## Install

```bash
otinstaller install cloud-enum
```

otinstaller installs the pip package `cloud-enum` pinned to version `0.1.0` in a dedicated virtualenv.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| domain (`d`) | `d:example.com` | `--domain example.com` |

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run cloud-enum -- --domain example.com
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run cloud-enum d:example.com
```

Results are saved to `./results/cloud-enum/<target>/`.
