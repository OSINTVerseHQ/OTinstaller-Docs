# Whatsapp Osint

WhatsApp spy - logs online/offline events from ANYONE in the world.

## Source

- Repository: https://github.com/jasperan/whatsapp-osint
- License: MIT

## Install

```bash
otinstaller install whatsapp-osint
```

otinstaller installs the pip package `whatsapp-osint` pinned to version `2.0.1` in a dedicated virtualenv.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| phone (`p`) | `p:+15551234567` | `--phone +15551234567` |

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run whatsapp-osint -- --phone +15551234567
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run whatsapp-osint p:+15551234567
```

Results are saved to `./results/whatsapp-osint/<target>/`.
