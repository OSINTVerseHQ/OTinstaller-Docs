# Crosslinked

LinkedIn enumeration tool to extract valid employee names from an organization through search engine scraping.

## Source

- Repository: https://github.com/m8sec/CrossLinked
- License: GPL-3.0

## Install

```bash
otinstaller install crosslinked
```

otinstaller installs the pip package `crosslinked` pinned to version `0.3.0` in a dedicated virtualenv.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| username (`u`) | `u:exampleuser` | `--username exampleuser` |
| email (`e`) | `e:example@example.com` | `--email example@example.com` |

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run crosslinked -- --username exampleuser --email example@example.com
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run crosslinked u:exampleuser e:example@example.com
```

Results are saved to `./results/crosslinked/<target>/`.
