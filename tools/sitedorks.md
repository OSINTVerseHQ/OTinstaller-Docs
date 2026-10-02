# Sitedorks

Search Google/Bing/Ecosia/DuckDuckGo/Yandex/Yahoo for a search term (dork) with a default set of websites, bug bounty programs or custom collection.

## Source

- Repository: https://github.com/Zarcolio/sitedorks
- License: GPL-3.0

## Install

```bash
otinstaller install sitedorks
```

otinstaller clones `https://github.com/Zarcolio/sitedorks.git` into a dedicated virtualenv, then installs the dependencies listed in `requirements.txt`.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| domain (`d`) | `d:example.com` | `--domain example.com` |
| url (`url`) | `url:https://example.com` | `--url https://example.com` |

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run sitedorks -- --domain example.com --url https://example.com
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run sitedorks d:example.com url:https://example.com
```

Results are saved to `./results/sitedorks/<target>/`.
