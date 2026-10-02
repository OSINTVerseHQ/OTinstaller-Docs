# Telepathy

OSINT toolkit for investigating Telegram chats and accounts. Requires Python <3.13 (dependency googletrans/httpx uses removed cgi module).

## Source

- Repository: https://github.com/telepathy/telepathy
- License: MIT

## Install

```bash
otinstaller install telepathy
```

otinstaller installs the pip package `telepathy` pinned to version `2.3.4` in a dedicated virtualenv.

## Credentials

Required keys: `TELEGRAM_API_ID`, `TELEGRAM_API_HASH`.

Keys are stored in `~/.otinstaller/.env`, one `KEY=value` per line. This tool only receives the keys listed above.

After install, otinstaller warns that this tool requires configuration: set these keys before the first run.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| username (`u`) | `u:exampleuser` | `--username exampleuser` |
| phone (`p`) | `p:+15551234567` | `--phone +15551234567` |

## Example output

```text
Telepathy example
Telegram chat analysis
Participants: 150
Messages analyzed: 5000
```

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run telepathy -- --username exampleuser --phone +15551234567
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run telepathy u:exampleuser p:+15551234567
```

Results are saved to `./results/telepathy/<target>/`.
