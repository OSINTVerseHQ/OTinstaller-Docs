# Aliens Eye

Hunt down 840+ social media accounts using AI.

## Source

- Repository: https://github.com/arxhr007/Aliens_eye
- License: MIT

## Install

```bash
otinstaller install aliens-eye
```

otinstaller installs the pip package `aliens_eye` pinned to version `2.5.0` in a dedicated virtualenv.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| username (`u`) | `u:exampleuser` | `--username exampleuser` |

## Example output

```text
aliens_eye v2.5.0 output for testuser (truncated):

AI-Enhanced Username Scanner - Find usernames across social media platforms

Scanning username: testuser

Selected profile (truncated):
  Found: github (https://github.com/testuser)
  Found: gitlab (https://gitlab.com/testuser)
  Found: twitter (https://twitter.com/testuser)
  Found: reddit (https://reddit.com/user/testuser)
  Found: youtube (https://youtube.com/@testuser)
  Found: pinterest (https://pinterest.com/testuser)
  Found: steam (https://steamcommunity.com/id/testuser)
  Found: spotify (https://spotify.com/user/testuser)
  Found: tiktok (https://tiktok.com/@testuser)
  Found: instagram (https://instagram.com/testuser)
  Found: patreon (https://patreon.com/testuser)
  Found: hackerrank (https://hackerrank.com/testuser)
  Found: leetcode (https://leetcode.com/testuser)
  Found: codeforces (https://codeforces.com/profile/testuser)
  Found: devto (https://dev.to/testuser)
  Found: medium (https://medium.com/@testuser)
  Found: twitch (https://twitch.tv/testuser)
  Found: discord (https://discord.com/users/testuser)
  Found: keybase (https://keybase.io/testuser)
  Found: linkedin (https://linkedin.com/in/testuser)
  Found: producthunt (https://producthunt.com/@testuser)
  Found: behance (https://behance.net/testuser)
  Found: dribbble (https://dribbble.com/testuser)
  Found: mastodon (https://mastodon.social/@testuser)
  Found: bluesky (https://bsky.app/profile/testuser)
  Found: codepen (https://codepen.io/testuser)
  Found: stackoverflow (https://stackoverflow.com/users/testuser)
  ... and 200+ more sites checked

╭──────────────────────────────── Scan Summary ────────────────────────────────╮
│ Found: 238   Maybe: 312   Not Found: 241   Errors: 49                        │
│ Scanned 840 sites in 81.3s                                                   │
╰──────────────────────────────────────────────────────────────────────────────╯
```

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run aliens-eye -- --username exampleuser
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run aliens-eye u:exampleuser
```

Results are saved to `./results/aliens-eye/<target>/`.
