# Instaloader

Download pictures (or videos) along with their captions and other metadata from Instagram.

## Source

- Repository: https://github.com/instaloader/instaloader
- License: MIT

## Install

```bash
otinstaller install instaloader
```

otinstaller installs the pip package `instaloader` pinned to version `4.15.4` in a dedicated virtualenv.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| username (`u`) | `u:exampleuser` | `exampleuser` (positional) |

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run instaloader -- exampleuser
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run instaloader u:exampleuser
```

Results are saved to `./results/instaloader/<target>/`.
