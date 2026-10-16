# Sublist3r

Fast subdomain enumeration tool using multiple search engines and certificate transparency logs.

## Source

- Repository: https://github.com/aboul3la/Sublist3r
- License: GPL-2.0

## Install

```bash
otinstaller install sublist3r
```

otinstaller clones `https://github.com/aboul3la/Sublist3r.git` at ref `729d649ec5370730172bf6f5314aafd68c874124` into a dedicated virtualenv, then installs the clone itself as a package.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| domain (`d`) | `d:example.com` | `--domain example.com` |

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run sublist3r -- --domain example.com
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run sublist3r d:example.com
```

Results are saved to `./results/sublist3r/<target>/`.
