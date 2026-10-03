# Openosint

AI-powered OSINT agent with interactive REPL, MCP server, and direct CLI modes. Direct email/username scans work without ANTHROPIC_API_KEY. AI-REPL and MCP modes require ANTHROPIC_API_KEY (or --api-key). Other features need additional keys: SHODAN_API_KEY (shodan), VIRUSTOTAL_API_KEY (virustotal), CENSYS_API_ID + CENSYS_SECRET (censys), ABUSEIPDB_API_KEY (abuseipdb), IP2LOCATION_API_KEY (ip2location), BRIGHTDATA_API_KEY + BRIGHTDATA_SERP_ZONE/BRIGHTDATA_UNLOCKER_ZONE (Bright Data tools), OPENAI_API_KEY (OpenAI provider), OPENOSINT_PROXY_URL (proxy).

## Source

- Repository: https://github.com/OpenOSINT/OpenOSINT
- License: MIT

## Install

```bash
otinstaller install openosint
```

otinstaller installs the pip package `openosint` pinned to version `2.30.0` in a dedicated virtualenv.

## Credentials

Optional keys: `ANTHROPIC_API_KEY`, `SHODAN_API_KEY`, `VIRUSTOTAL_API_KEY`, `CENSYS_API_ID`, `CENSYS_SECRET`, `ABUSEIPDB_API_KEY`, `IP2LOCATION_API_KEY`, `BRIGHTDATA_API_KEY`, `BRIGHTDATA_SERP_ZONE`, `BRIGHTDATA_UNLOCKER_ZONE`, `OPENAI_API_KEY`, `OPENOSINT_PROXY_URL`.

Keys are stored in `~/.otinstaller/.env`, one `KEY=value` per line. This tool only receives the keys listed above.

## Run

```bash
otinstaller run openosint -- --help
```

Results are saved to `./results/openosint/<target>/`.
