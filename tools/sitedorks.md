# Sitedorks

Search Google/Bing/Ecosia/DuckDuckGo/Yandex/Yahoo for a search term (dork) with a default set of websites, bug bounty programs or custom collection.

## Source

- Repository: https://github.com/Zarcolio/sitedorks
- License: GPL-3.0

## Install

```bash
otinstaller install sitedorks
```

otinstaller clones `https://github.com/Zarcolio/sitedorks.git` at ref `ce6421a963d50c3b18128052703274552d284d94` into a dedicated virtualenv, then installs the dependencies listed in `requirements.txt`.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| query (`q`) | `q:example` | `-query example` |

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run sitedorks -- -query example
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run sitedorks q:example
```

Results are saved to `./results/sitedorks/<target>/`.
