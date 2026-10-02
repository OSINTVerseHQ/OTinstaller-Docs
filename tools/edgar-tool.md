# EDGAR Tool

Command line interface to search and retrieve corporate and financial data from the SEC EDGAR database.

## Source

- Repository: https://github.com/bellingcat/edgar
- License: MIT

## Install

```bash
otinstaller install edgar-tool
```

otinstaller installs the pip package `edgar-tool` pinned to version `2.1.2` in a dedicated virtualenv.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| query (`q`) | `q:example` | `text-search example` |
| domain (`d`) | `d:example.com` | `example.com` (positional) |

## Example output

```text
EDGAR Tool example
Company: Example Corp
CIK: 1234567
Filings: 10-K, 10-Q
```

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run edgar-tool -- text-search example example.com
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run edgar-tool q:example d:example.com
```

Results are saved to `./results/edgar-tool/<target>/`.
