# Ctfr

Abusing Certificate Transparency logs for getting HTTPS websites subdomains.

## Source

- Repository: https://github.com/UnaPibaGeek/ctfr
- License: GPL-3.0

## Install

```bash
otinstaller install ctfr
```

otinstaller clones `https://github.com/UnaPibaGeek/ctfr.git` into a dedicated virtualenv, then installs the dependencies listed in `requirements.txt`.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| domain (`d`) | `d:example.com` | `--domain example.com` |

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run ctfr -- --domain example.com
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run ctfr d:example.com
```

Results are saved to `./results/ctfr/<target>/`.
