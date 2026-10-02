# H8Mail

Email OSINT & Password breach hunting tool, locally or using premium services.

## Source

- Repository: https://github.com/khast3x/h8mail
- License: NOASSERTION

## Install

```bash
otinstaller install h8mail
```

otinstaller installs the pip package `h8mail` pinned to version `2.5.6` in a dedicated virtualenv.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| email (`e`) | `e:example@example.com` | `--email example@example.com` |

## Example output

```text
h8mail v2.5.6 output for test@example.com:

h8mail is up to date
Removing duplicates
Targets:
test@example.com
scylla.so is down, skipping
Target factory started for test@example.com
[test@example.com]>[hunter.io public]
hunter.io (public API) error: test@example.com 'data'

Showing results for test@example.com
No results founds

Session Recap:

Target                  | Status
test@example.com        | Not Compromised

Execution time: 1.69 seconds
```

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run h8mail -- --email example@example.com
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run h8mail e:example@example.com
```

Results are saved to `./results/h8mail/<target>/`.
