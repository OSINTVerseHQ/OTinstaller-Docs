# Auto Archiver

Automatically archive web content from various sources. Requires Python <3.13 (no wheels for 3.13+; dependency pdqhash needs C++ compiler).

## Source

- Repository: https://github.com/bellingcat/auto-archiver
- License: MIT

## Install

```bash
otinstaller install auto-archiver
```

otinstaller installs the pip package `auto-archiver` pinned to version `1.2.9` in a dedicated virtualenv.

## Credentials

Required keys: `GOOGLE_API_KEY`, `GOOGLE_CREDENTIALS`.
Optional keys: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`.

Keys are stored in `~/.otinstaller/.env`, one `KEY=value` per line. This tool only receives the keys listed above.

After install, otinstaller warns that this tool requires configuration: set these keys before the first run.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| url (`url`) | `url:https://example.com` | `--url https://example.com` |

## Example output

```text
Auto Archiver example
URL: https://example.com
Archived to: archive.example.com/abc123
```

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run auto-archiver -- --url https://example.com
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run auto-archiver url:https://example.com
```

Results are saved to `./results/auto-archiver/<target>/`.
