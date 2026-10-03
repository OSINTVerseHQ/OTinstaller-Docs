# Sublist3r

Fast subdomain enumeration tool using multiple search engines and certificate transparency logs.

## Source

- Repository: https://github.com/aboul3la/Sublist3r
- License: GPL-2.0

## Install

```bash
otinstaller install sublist3r
```

otinstaller installs the pip package `sublist3r` pinned to version `1.0` in a dedicated virtualenv.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| domain (`d`) | `d:example.com` | `--domain example.com` |

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run sublist3r -- --domain example.com
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run sublist3r d:example.com
```

Results are saved to `./results/sublist3r/<target>/`.
