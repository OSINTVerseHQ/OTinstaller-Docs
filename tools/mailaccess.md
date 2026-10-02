# Mailaccess

Free email OSINT tool, 2500+ platforms, identity clustering, breach detection.

## Source

- Repository: https://github.com/KatrielMoses/MailAccess
- License: unknown

## Install

```bash
otinstaller install mailaccess
```

otinstaller installs the pip package `mailaccess` pinned to version `0.17.6` in a dedicated virtualenv.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| email (`e`) | `e:example@example.com` | `--email example@example.com` |

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run mailaccess -- --email example@example.com
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run mailaccess e:example@example.com
```

Results are saved to `./results/mailaccess/<target>/`.
