# Paramspider

Mining URLs from dark corners of Web Archives for bug hunting/fuzzing/further probing.

## Source

- Repository: https://github.com/devanshbatham/ParamSpider
- License: MIT

## Install

```bash
otinstaller install paramspider
```

otinstaller clones `https://github.com/devanshbatham/ParamSpider.git` into a dedicated virtualenv, then installs the clone itself as a package.

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
otinstaller run paramspider -- --domain example.com --url https://example.com
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run paramspider d:example.com url:https://example.com
```

Results are saved to `./results/paramspider/<target>/`.
