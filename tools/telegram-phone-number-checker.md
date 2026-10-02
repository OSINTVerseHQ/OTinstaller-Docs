# Telegram Phone Number Checker

Check if phone numbers are connected to Telegram accounts.

## Source

- Repository: https://github.com/bellingcat/telegram-phone-number-checker
- License: MIT

## Install

```bash
otinstaller install telegram-phone-number-checker
```

otinstaller installs the pip package `telegram-phone-number-checker` pinned to version `1.2.2` in a dedicated virtualenv.

## Credentials

Required keys: `TELEGRAM_API_ID`, `TELEGRAM_API_HASH`.

Keys are stored in `~/.otinstaller/.env`, one `KEY=value` per line. This tool only receives the keys listed above.

After install, otinstaller warns that this tool requires configuration: set these keys before the first run.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| phone (`p`) | `p:+15551234567` | `--phone-numbers +15551234567` |
| username (`u`) | `u:exampleuser` | `--usernames exampleuser` |

## Example output

```text
Telegram Phone Number Checker example
Phone: +15551234567
Result: Found on Telegram
Username: johndoe
```

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run telegram-phone-number-checker -- --phone-numbers +15551234567 --usernames exampleuser
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run telegram-phone-number-checker p:+15551234567 u:exampleuser
```

Results are saved to `./results/telegram-phone-number-checker/<target>/`.
