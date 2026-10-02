# Instagram Monitor

Track Instagram users' activities, profile changes and capture content with beautiful dashboards and instant notifications.

## Source

- Repository: https://github.com/misiektoja/instagram_monitor
- License: GPL-3.0

## Install

```bash
otinstaller install instagram-monitor
```

otinstaller installs the pip package `instagram_monitor` pinned to version `4.0.2` in a dedicated virtualenv.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| username (`u`) | `u:exampleuser` | `--username exampleuser` |

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run instagram-monitor -- --username exampleuser
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run instagram-monitor u:exampleuser
```

Results are saved to `./results/instagram-monitor/<target>/`.
