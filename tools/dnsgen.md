# Dnsgen

DNSGen is a powerful and flexible DNS name permutation tool designed for security researchers and penetration testers.

## Source

- Repository: https://github.com/AlephNullSK/dnsgen
- License: MIT

## Install

```bash
otinstaller install dnsgen
```

otinstaller installs the pip package `dnsgen` pinned to version `1.0.4` in a dedicated virtualenv.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| domain (`d`) | `d:example.com` | `--domain example.com` |

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run dnsgen -- --domain example.com
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run dnsgen d:example.com
```

Results are saved to `./results/dnsgen/<target>/`.
