# API keys

One env file holds all API keys: `~/.otinstaller/.env`, permissions 600. From that file, each tool only receives the keys it declares in its registry entry. Tools also inherit your shell environment, so do not export secrets you do not want tools to see. Run `otinstaller keys check` to verify your keys.

_This page mirrors the [OTinstaller README](https://github.com/OSINTVerseHQ/OTinstaller)._
