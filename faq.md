# FAQ

**Does it work on Windows or macOS?**
On Windows, yes, inside WSL2 with Ubuntu. macOS is not tested yet, and most of the tools are built for Linux first.

**Do I need root?**
No. Root is only needed once, for `sudo apt install python3-venv git`. Everything else lives in your home directory under `~/.otinstaller/`.

**Does OTinstaller send my data anywhere?**
OTinstaller itself only contacts GitHub and PyPI, to install and update tools. There is no telemetry. The tools you run contact the services they are built to query.

**How do I uninstall it?**
`ot remove --all` removes every tool, then `pipx uninstall otinstaller` removes OTinstaller itself. `rm -rf ~/.otinstaller` deletes the config, the API key file and the logs. Results stay wherever you ran your commands.

**Is it legal to use?**
The tools are legal to install. Whether a particular use is legal depends on where you are and what you are investigating. Read [Responsible use](guides/responsible-use.md) before running anything against a real person.

_This page mirrors the [OTinstaller README](https://github.com/OSINTVerseHQ/OTinstaller)._
