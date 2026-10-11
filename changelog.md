# Changelog

## Unreleased

### Added

- Startup banner for `otinstaller init`, `otinstaller about` and a bare `otinstaller`
  call. It is only shown in an interactive terminal, never with `--json` or when
  output is piped, and `OTINSTALLER_NO_BANNER=1` turns it off.
- `long_running` registry field. Tools that monitor a target continuously
  (`whatsapp-osint`, `instagram-monitor`) are no longer started by `run --all` or
  `auto`.

### Fixed

- Typed inputs now map to each tool's real flags. Every mapping was checked by
  running the tool with the typed input. Tools whose input cannot be expressed as a
  single typed value no longer advertise one; pass their arguments after `--`.
- `spiderfoot` now runs the `sf.py` scanner in passive mode instead of the
  `sfcli.py` client.
- `ghunt` and `toutatis` are marked as needing configuration (a Google login and an
  Instagram session ID respectively).

### Removed

- `cloud-enum`: the pinned PyPI release does not exist.

## 0.0.1

- First release on PyPI.
