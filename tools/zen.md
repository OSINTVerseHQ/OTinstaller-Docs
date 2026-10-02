# Zen

Find email addresses of GitHub users, repositories and organizations.

## Source

- Repository: https://github.com/s0md3v/Zen
- License: Apache-2.0

## Install

```bash
otinstaller install zen
```

otinstaller clones `https://github.com/s0md3v/Zen.git` into a dedicated virtualenv, then installs the dependencies listed in `requirements.txt`.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| username (`u`) | `u:exampleuser` | `exampleuser` (positional) |
| url (`url`) | `url:https://example.com` | `https://example.com` (positional) |

## Example output

```text
example output for zen:
------------------------------------------------------------
	Z E N v1.0

[!] Total contributors: 3
contributor1 : dev1@example.com
contributor2 : dev2@example.com

octocat : octocat@users.noreply.github.com
------------------------------------------------------------
(Example trimmed - real output starts with a green banner)
```

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run zen -- exampleuser https://example.com
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run zen u:exampleuser url:https://example.com
```

Results are saved to `./results/zen/<target>/`.
