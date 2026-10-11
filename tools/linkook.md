# Linkook

An OSINT tool for discovering linked social accounts and associated emails across multiple platforms using a single username.

## Source

- Repository: https://github.com/JackJuly/linkook
- License: MIT

## Install

```bash
otinstaller install linkook
```

otinstaller installs the pip package `linkook` pinned to version `1.1.2` in a dedicated virtualenv.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| username (`u`) | `u:exampleuser` | `exampleuser` (positional) |

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run linkook -- exampleuser
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run linkook u:exampleuser
```

Results are saved to `./results/linkook/<target>/`.
