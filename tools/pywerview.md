# Pywerview

A (partial) Python rewriting of PowerSploit's PowerView.

## Source

- Repository: https://github.com/the-useless-one/pywerview
- License: GPL-3.0

## Install

```bash
otinstaller install pywerview
```

otinstaller installs the pip package `pywerview` pinned to version `0.7.6` in a dedicated virtualenv.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| domain (`d`) | `d:example.com` | `--domain example.com` |
| username (`u`) | `u:exampleuser` | `--username exampleuser` |

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run pywerview -- --domain example.com --username exampleuser
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run pywerview d:example.com u:exampleuser
```

Results are saved to `./results/pywerview/<target>/`.
