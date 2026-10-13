# Mailaccess

Free email OSINT tool, 2500+ platforms, identity clustering, breach detection. BROKEN: crashes on --help (missing greenlet dependency), has placeholder URLs, unknown license.

## Source

- Repository: https://github.com/KatrielMoses/MailAccess
- License: unknown

## Install

```bash
otinstaller install mailaccess
```

otinstaller installs the pip package `mailaccess` pinned to version `0.18.5` in a dedicated virtualenv.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| email (`e`) | `e:example@example.com` | `example@example.com` (positional) |

otinstaller always adds these arguments first: `--no-banner investigate`.

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run mailaccess -- --no-banner investigate example@example.com
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run mailaccess e:example@example.com
```

Results are saved to `./results/mailaccess/<target>/`.
