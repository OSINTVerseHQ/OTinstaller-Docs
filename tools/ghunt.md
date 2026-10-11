# Ghunt

Offensive Google framework.

## Source

- Repository: https://github.com/mxrch/GHunt
- License: NOASSERTION

## Install

```bash
otinstaller install ghunt
```

otinstaller installs the pip package `ghunt` pinned to version `2.3.4` in a dedicated virtualenv.

## Credentials

No API keys needed.

This tool still needs manual configuration before the first run.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| email (`e`) | `e:example@example.com` | `example@example.com` (positional) |

otinstaller always adds these arguments first: `email`.

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run ghunt -- email example@example.com
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run ghunt e:example@example.com
```

Results are saved to `./results/ghunt/<target>/`.
