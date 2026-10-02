# Yark

OSINT for YouTube made simple.

## Source

- Repository: https://github.com/Owez/yark
- License: MIT

## Install

```bash
otinstaller install yark
```

otinstaller installs the pip package `yark` pinned to version `1.2.12` in a dedicated virtualenv.

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
otinstaller run yark -- --url https://example.com --username exampleuser
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run yark url:https://example.com u:exampleuser
```

Results are saved to `./results/yark/<target>/`.
