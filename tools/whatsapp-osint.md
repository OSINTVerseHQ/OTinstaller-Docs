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

This tool still needs manual configuration before the first run.

This tool monitors its target continuously and does not exit on its own. It is never started by `otinstaller run --all` or `otinstaller auto`; run it by name and stop it with Ctrl+C.

## Run

```bash
otinstaller run whatsapp-osint -- --help
```

Results are saved to `./results/whatsapp-osint/<target>/`.
