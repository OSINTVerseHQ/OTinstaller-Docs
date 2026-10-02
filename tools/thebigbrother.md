# The Big Brother

Find usernames across social networks.

## Source

- Repository: https://github.com/chadi0x/TheBigBrother
- License: MIT

## Install

```bash
otinstaller install thebigbrother
```

otinstaller clones `https://github.com/chadi0x/TheBigBrother.git` into a dedicated virtualenv, then installs the clone itself as a package.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| username (`u`) | `u:exampleuser` | `exampleuser` (positional) |

## Example output

```text
example output for thebigbrother:
------------------------------------------------------------
[*] Checking username testuser on:

[+] 9GAG: https://www.9gag.com/u/testuser
[+] About.me: https://about.me/testuser
[+] Bluesky: https://bsky.app/profile/testuser.bsky.social
[+] GitLab: https://gitlab.com/testuser
[+] HackerNews: https://news.ycombinator.com/user?id=testuser
[+] Reddit: https://reddit.com/user/testuser
[+] Telegram: https://t.me/testuser
[+] Twitch: https://www.twitch.tv/testuser
[+] YouTube: https://www.youtube.com/@testuser

[*] Search completed with 178 results
------------------------------------------------------------
(Example trimmed - real output lists every site found)
```

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run thebigbrother -- exampleuser
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run thebigbrother u:exampleuser
```

Results are saved to `./results/thebigbrother/<target>/`.
