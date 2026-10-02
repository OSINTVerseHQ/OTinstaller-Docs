# Secator

secator - the pentester's swiss knife.

## Source

- Repository: https://github.com/freelabz/secator
- License: NOASSERTION

## Install

```bash
otinstaller install secator
```

otinstaller installs the pip package `secator` pinned to version `0.45.0` in a dedicated virtualenv.

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
otinstaller run secator -- --domain example.com --username exampleuser --email example@example.com
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run secator d:example.com u:exampleuser e:example@example.com
```

Results are saved to `./results/secator/<target>/`.
