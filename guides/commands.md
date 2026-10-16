# Command reference

| Command | What it does |
| --- | --- |
| `otinstaller init` | Create config and directories, accept the notice |
| `otinstaller list` / `--installed` | List tools |
| `otinstaller search <query>` | Search tools |
| `otinstaller info <tool>` or `otinstaller <tool>` | Show tool details |
| `otinstaller install <tool>...` / `--all` | Install tools |
| `otinstaller run <tool>... -- <args>` | Run tools |
| `otinstaller run --all u:...` | Run all matching tools |
| `otinstaller run --live` | Live status table for parallel runs |
| `otinstaller run --case <name>` | Group runs under a named case |
| `otinstaller auto <target>` | Detect the target type and run matching tools |
| `otinstaller playbook [name] [target]` / `--list` | Run or list playbooks |
| `otinstaller example <tool>` | Show example output |
| `otinstaller extract <target>` | Extract indicators from saved results |
| `otinstaller diff <tool> <target>` | Compare the two most recent runs |
| `otinstaller update` / `--all` / `--check-only` | Bring tools to the version this release of otinstaller pins and tested |
| `otinstaller check-updates` | Check for updates (read-only) |
| `otinstaller remove <tool>...` / `--all` | Remove tools |
| `otinstaller keys check` | Check API keys |
| `otinstaller crash-reports` / `on` / `off` | Show or change opt-in crash reports (off by default) |
| `otinstaller resume` | Handle interrupted jobs |
| `otinstaller doctor` | Check the machine |
| `otinstaller about` | Show the banner, credits and contact |

### Scripts and AI agents

Every command supports `--json`. Commands never prompt when `--yes` or `-y` is given, or when stdin is not a terminal. otinstaller's own errors exit with 1 (error), 2 (invalid input) or 130 (interrupted). For a single-tool run, the tool's own exit code is returned and also recorded in the `.meta.json` file.

The startup banner is only shown in an interactive terminal. It is never printed with `--json` or when output is piped, and `OTINSTALLER_NO_BANNER=1` turns it off completely.

For AI agents, see [`llms.txt`](https://github.com/OSINTVerseHQ/OTinstaller/blob/main/llms.txt).

_This page mirrors the [OTinstaller README](https://github.com/OSINTVerseHQ/OTinstaller)._
