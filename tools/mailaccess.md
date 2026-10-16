# Mailaccess

Investigates an email address across 5,300+ platforms and breach sources, and harvests the email addresses of a domain

## Source

- Repository: https://github.com/KatrielMoses/MailAccess
- License: MIT

## Install

```bash
otinstaller install mailaccess
```

otinstaller installs the pip package `mailaccess` pinned to version `0.18.7` in a dedicated virtualenv. It also installs `mailaccess[browser]==0.18.7` and `playwright>=1.49`. Then Playwright downloads Chromium (the headless shell) into the tool's own folder, so `otinstaller remove` deletes it too.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| email (`e`) | `e:example@example.com` | `investigate example@example.com` |
| domain (`d`) | `d:example.com` | `harvest-emails --domain example.com` |

otinstaller always adds these arguments first: `--no-banner`.

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run mailaccess -- investigate example@example.com
otinstaller run mailaccess -- harvest-emails --domain example.com
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run mailaccess e:example@example.com
otinstaller run mailaccess d:example.com
```

Results are saved to `./results/mailaccess/<target>/`.

## Harvest a domain's email addresses

`d:` runs MailAccess's `harvest-emails`. It looks for the email addresses of a domain in Common Crawl, certificate logs, PGP keyservers, package registries, code hosts, subdomains and search results, then guesses the domain's address pattern and checks the results.

```bash
otinstaller run mailaccess d:example.com
```

Add MailAccess's own options after `--`:

```bash
# Skip the SMTP check and run fewer searches, for a quick first look
otinstaller run mailaccess -- harvest-emails --domain example.com --no-verify --lite

# Save the full harvest as JSON, and only show addresses rated high
otinstaller run mailaccess -- harvest-emails --domain example.com --export harvest.json --min-confidence high
```

By default MailAccess checks found addresses with SMTP `RCPT TO`: it connects to the domain's mail servers from your network but sends no email. `--no-verify` skips this. `--timeout <seconds>` limits how long a harvest runs. `otinstaller run mailaccess -- harvest-emails --help` lists every option.

## Investigate an email address

`e:` runs `investigate`, which checks the address against breach sources and thousands of platforms and prints a report. Some of those checks run in a headless browser; otinstaller installs the browser with MailAccess, so they run instead of being skipped.

```bash
# Also save the report as Markdown (or .json, .csv, .stix for STIX 2.1, .mtgx for Maltego)
otinstaller run mailaccess -- investigate someone@example.com -o report.md
```

`otinstaller run mailaccess -- investigate --help` lists every option, and `otinstaller run mailaccess -- --help` lists MailAccess's other commands. Optional API keys add more sources; MailAccess keeps them itself (`otinstaller run mailaccess -- keys --help`).

If the browser checks show as skipped, Chromium may be missing system libraries. On Debian, Ubuntu and Kali this installs them:

```bash
sudo ~/.otinstaller/tools/mailaccess/venv/bin/python -m playwright install-deps chromium
```
