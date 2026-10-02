# Openosint

AI-powered OSINT agent with interactive REPL, MCP server, and CLI.

## Source

- Repository: https://github.com/OpenOSINT/OpenOSINT
- License: MIT

## Install

```bash
otinstaller install openosint
```

otinstaller installs the pip package `openosint` pinned to version `2.29.0` in a dedicated virtualenv.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| username (`u`) | `u:exampleuser` | `--username exampleuser` |
| email (`e`) | `e:example@example.com` | `--email example@example.com` |
| domain (`d`) | `d:example.com` | `--domain example.com` |

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run openosint -- --username exampleuser --email example@example.com --domain example.com
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run openosint u:exampleuser e:example@example.com d:example.com
```

Results are saved to `./results/openosint/<target>/`.
