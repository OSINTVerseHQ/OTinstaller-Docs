# Instaloader

Download pictures (or videos) along with their captions and other metadata from Instagram.

## Source

- Repository: https://github.com/instaloader/instaloader
- License: MIT

## Install

```bash
otinstaller install instaloader
```

otinstaller installs the pip package `instaloader` pinned to version `4.15.3` in a dedicated virtualenv.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| username (`u`) | `u:exampleuser` | `--username exampleuser` |
| url (`url`) | `url:https://example.com` | `--url https://example.com` |

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run instaloader -- --username exampleuser --url https://example.com
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run instaloader u:exampleuser url:https://example.com
```

Results are saved to `./results/instaloader/<target>/`.
