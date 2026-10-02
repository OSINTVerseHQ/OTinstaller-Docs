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
| username (`u`) | `u:exampleuser` | `--username exampleuser` |
| email (`e`) | `e:example@example.com` | `--email example@example.com` |

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run linkook -- --username exampleuser --email example@example.com
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run linkook u:exampleuser e:example@example.com
```

Results are saved to `./results/linkook/<target>/`.
