# Fsociety

A Modular Penetration Testing Framework.

## Source

- Repository: https://github.com/fsociety-team/fsociety
- License: MIT

## Install

```bash
otinstaller install fsociety
```

otinstaller installs the pip package `fsociety` pinned to version `3.2.9` in a dedicated virtualenv.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| domain (`d`) | `d:example.com` | `--domain example.com` |
| username (`u`) | `u:exampleuser` | `--username exampleuser` |
| email (`e`) | `e:example@example.com` | `--email example@example.com` |

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run fsociety -- --domain example.com --username exampleuser --email example@example.com
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run fsociety d:example.com u:exampleuser e:example@example.com
```

Results are saved to `./results/fsociety/<target>/`.
