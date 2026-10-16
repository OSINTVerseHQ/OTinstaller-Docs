# Telepathy

OSINT toolkit for investigating Telegram chats and accounts. Requires Python <3.13 (dependency googletrans/httpx uses removed cgi module).

## Source

- Repository: https://github.com/prose-intelligence-ltd/Telepathy-Community
- License: MIT

## Install

```bash
otinstaller install telepathy
```

otinstaller installs the pip package `telepathy` pinned to version `2.3.4` in a dedicated virtualenv.

## Credentials

No API keys needed.

This tool still needs manual configuration before the first run.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| telegram channel (`tg`) | `tg:examplechannel` | `-t examplechannel` |

## Example output

Illustrative output showing the general shape of a run. Real output depends on the tool version and the target.

```text
Telepathy example
Telegram chat analysis
Participants: 150
Messages analyzed: 5000
```

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run telepathy -- -t examplechannel
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run telepathy tg:examplechannel
```

Results are saved to `./results/telepathy/<target>/`.
