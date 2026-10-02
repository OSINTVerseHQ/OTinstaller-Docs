# Blackbird

OSINT tool to search for accounts by username and email across social networks.

## Source

- Repository: https://github.com/p1ngul1n0/blackbird
- License: GPL-3.0

## Install

```bash
otinstaller install blackbird
```

otinstaller clones `https://github.com/p1ngul1n0/blackbird.git` into a dedicated virtualenv, then installs the dependencies listed in `requirements.txt`.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| username (`u`) | `u:exampleuser` | `--username exampleuser` |
| email (`e`) | `e:example@example.com` | `--email example@example.com` |

## Example output

```text
Blackbird example output
Username: johndoe
Found on: Twitter, GitHub, LinkedIn
```

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run blackbird -- --username exampleuser --email example@example.com
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run blackbird u:exampleuser e:example@example.com
```

Results are saved to `./results/blackbird/<target>/`.
