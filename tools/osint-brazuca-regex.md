# Osint Brazuca Regex

Repositrio criado com intuito de reunir expresses regulares dentro do contexto Brasil.

## Source

- Repository: https://github.com/osintbrazuca/osint-brazuca-regex
- License: MIT

## Install

```bash
otinstaller install osint-brazuca-regex
```

otinstaller clones `https://github.com/osintbrazuca/osint-brazuca-regex.git` into a dedicated virtualenv, then installs the dependencies listed in `requirements.txt`.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| domain (`d`) | `d:example.com` | `--domain example.com` |

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run osint-brazuca-regex -- --domain example.com
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run osint-brazuca-regex d:example.com
```

Results are saved to `./results/osint-brazuca-regex/<target>/`.
