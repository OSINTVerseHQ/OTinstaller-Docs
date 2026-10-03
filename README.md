# OTinstaller

OTinstaller is a command line tool manager for Linux. It installs, runs, updates,
and removes open-source command line tools by name, each in its own virtualenv,
through one standard command interface.

You pick a tool by name. otinstaller installs it, runs it against a target, and
saves the output under `./results/` with a metadata sidecar file. You do not learn
a different install method for every tool.

This site covers 47 tools. The tool list focuses on open-source intelligence
(OSINT) tooling and is rebuilt from the otinstaller registry whenever the registry
changes. A tool only appears here after it passes an automated install test and a
smoke test.

## Contents

- [Getting started](getting-started.md): install otinstaller, run `otinstaller
  init`, and run your first tool.
- [Tools](SUMMARY.md): one page per tool with source, install method, credentials,
  input flags, example output, and run commands.
