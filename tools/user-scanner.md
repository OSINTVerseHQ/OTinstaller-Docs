# User Scanner

(2-in-1) Email & Username OSINT suite featuring native MCP support for deep data extraction just from a single Email/Username.

## Source

- Repository: https://github.com/kaifcodec/user-scanner
- License: MIT

## Install

```bash
otinstaller install user-scanner
```

otinstaller installs the pip package `user-scanner` pinned to version `1.5.2` in a dedicated virtualenv.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| username (`u`) | `u:exampleuser` | `--username exampleuser` |
| email (`e`) | `e:example@example.com` | `--email example@example.com` |

## Example output

```text
user-scanner v1.5.2 output for testuser (truncated):

Checking username: testuser

== LEARNING SITES ==
  [✔] Orcid: Found
  [✔] Endnote: Found
  [✔] Duolingo: Found
  [✔] Openalex: Found

== DEV SITES ==
  [✔] Hackerearth: Found
  [✔] Sourceforge: Found
  [✔] Codewars: Found
  [✔] Scratch: Found
  [✔] Codeberg: Found
  [✔] Gitlab: Found
  [✔] Tryhackme: Found
  [✔] Codeforces: Found
  [✔] Leetcode: Found
  [✔] Atcoder: Found
  [✔] Npmjs: Found
  [✔] Rubygems: Found
  [✔] Hackerrank: Found
  [✔] Gitea: Found

== ENTERTAINMENT SITES ==
  [✔] Rocketbeans: Found

== OTHER SITES ==
  [✔] Zomato: Found
  [✔] Pastebin: Found
  [✔] Trello: Found
  [✔] Wordpress: Found

== EMAIL SITES ==
  [✔] Protonmail: Found

== COMMUNITY SITES ==
  [✔] Viblo.asia: Found
  [✔] Stackoverflow: Found
  [✔] Wikipedia: Found
  [✔] Fandom: Found
  [✔] Hackernews: Found

== SHOPPING SITES ==
  [✔] Themeforest: Found
  [✔] Vinted: Found

== FINANCE SITES ==
  [✔] Etoro: Found
  [✔] Tradingview: Found
  [✔] Paypal: Found

== ADULT SITES ==
  [✔] E621: Found
  [✔] Xhamster: Found
  [✔] Pornhub: Found
  [✔] Xvideos: Found

== DONATION SITES ==
  [✔] Kofi: Found
  [✔] Buymeacoffee: Found

== CREATOR SITES ==
  [✔] Linktree: Found
  [✔] Vimeo: Found
  [✔] Substack: Found
  [✔] Producthunt: Found
  [✔] Devto: Found
  [✔] Kaggle: Found
  [✔] Twitch: Found
  [✔] Bluesky: Found
  [✔] X (twitter): Found
  [✔] Pinterest: Found
  [✔] Goodreads: Found
  [✔] Letterboxd: Found

== GAMING SITES ==
  [✔] Minecraft: Found
  [✔] Steam: Found
  [✔] Osu: Found
  [✔] Medal: Found
  [✔] Roblox: Found
  [✔] Lichess: Found
  [✔] Chess.com: Found

== SOCIAL SITES ==
  [✔] Youtube: Found
  [✔] Keybase: Found
  [✔] Telegram: Found
  [✔] Discord: Found
  [✔] Instagram: Found
  [✔] LinkedIn: Found
  [✔] Bluesky: Found
  [✔] Mastodon: Found

== MUSIC SITES ==
  [✔] Lastfm: Found
  [✔] Discogs: Found
  [✔] Bandcamp: Found
  [✔] Soundcloud: Found

== CREATIVE SITES ==
  [✔] Deviantart: Found
  [✔] Flickr: Found
  [✔] Unsplash: Found

== POLITICAL SITES ==
  [✔] Bitchute: Found

[i] Scan complete.
  Total hits: 202
```

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run user-scanner -- --username exampleuser --email example@example.com
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run user-scanner u:exampleuser e:example@example.com
```

Results are saved to `./results/user-scanner/<target>/`.
