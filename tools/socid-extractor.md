# Socid Extractor

The extraction engine behind Maigret: turn any profile URL into a structured OSINT record across 150+ sites.

## Source

- Repository: https://github.com/soxoj/socid-extractor
- License: MIT

## Install

```bash
otinstaller install socid-extractor
```

otinstaller installs the pip package `socid-extractor` pinned to version `0.1.1` in a dedicated virtualenv.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| url (`url`) | `url:https://example.com` | `--url https://example.com` |
| username (`u`) | `u:exampleuser` | `--username exampleuser` |

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run socid-extractor -- --url https://example.com --username exampleuser
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run socid-extractor url:https://example.com u:exampleuser
```

Results are saved to `./results/socid-extractor/<target>/`.
