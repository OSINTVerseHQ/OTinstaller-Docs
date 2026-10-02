# Instagram Location Search

Find Instagram location IDs near specified coordinates.

## Source

- Repository: https://github.com/bellingcat/instagram-location-search
- License: MIT

## Install

```bash
otinstaller install instagram-location-search
```

otinstaller installs the pip package `instagram-location-search` pinned to version `1.5.2` in a dedicated virtualenv.

## Credentials

Optional keys: `INSTAGRAM_SESSION_ID`.

Keys are stored in `~/.otinstaller/.env`, one `KEY=value` per line. This tool only receives the keys listed above.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| latitude (`lat`) | `lat:40.7128` | `--lat 40.7128` |
| longitude (`lng`) | `lng:-74.0060` | `--lng -74.0060` |

## Example output

```text
Instagram Location Search example
Coordinates: 32.22 N, 110.97 W
Locations: Tucson, Arizona
```

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run instagram-location-search -- --lat 40.7128 --lng -74.0060
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run instagram-location-search lat:40.7128 lng:-74.0060
```

Results are saved to `./results/instagram-location-search/<target>/`.
