# Torbot

Dark Web OSINT Tool.

## Source

- Repository: https://github.com/DedSecInside/TorBot
- License: NOASSERTION

## Install

```bash
otinstaller install torbot
```

otinstaller installs the pip package `torbot` pinned to version `4.3.0` in a dedicated virtualenv.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| url (`url`) | `url:https://example.com` | `--url https://example.com` |
| domain (`d`) | `d:example.com` | `--domain example.com` |

## Example output

```text
TorBot v4.3.0 output for http://example.com (with --disable-socks5):

TorBot - Dark Web OSINT Tool
GitHub: https://github.com/DedsecInside/TorBot
LICENSE: GNU Public License v3

Sorry. You are not using Tor.
Your IP address appears to be: 36.255.185.133

Title                  URL                                    Status                 Phone Numbers    Emails    Category
---------------------  -------------------------------------  ---------------------  ---------------  --------  ------------------------
Example Domain         http://example.com                     200 OK                 []               []        Business/Corporate
301 Moved Permanently  https://iana.org/help/example-domains  301 Moved Permanently  []               []        Computers and Technology
```

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run torbot -- --url https://example.com --domain example.com
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run torbot url:https://example.com d:example.com
```

Results are saved to `./results/torbot/<target>/`.
