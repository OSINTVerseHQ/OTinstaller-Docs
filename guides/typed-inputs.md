# Typed inputs

Instead of remembering each tool's flags, use a typed input prefix:

| Prefix | Input | Example |
| --- | --- | --- |
| `u:` | username | `u:johndoe` |
| `e:` | email | `e:john@example.com` |
| `p:` | phone | `p:+15551234567` |
| `d:` | domain | `d:example.com` |
| `url:` | URL | `url:https://example.com` |
| `q:` | text query | `q:search terms` |
| `geo:` | coordinates | `geo:32.22,-110.97` |
| `tg:` | Telegram channel | `tg:channelname` |
| `lat:` | latitude | `lat:37.7749` |
| `lng:` | longitude | `lng:-122.4194` |

```bash
otinstaller run sherlock -- u:johndoe
otinstaller run holehe -- e:john@example.com
otinstaller run dnstwist -- d:example.com
```

A tool can do something different for each input. MailAccess investigates an email address with `e:` and harvests the email addresses of a domain with `d:`:

```bash
otinstaller run mailaccess -- e:john@example.com
otinstaller run mailaccess -- d:example.com
```

Each tool declares which input types it supports. Run `otinstaller info <tool>` to see its mapping. Plain arguments after `--` are always passed to the tool unchanged, so every flag of the original tool still works.

## Run every matching tool

```bash
otinstaller run --all u:johndoe
otinstaller run --all --live e:john@example.com
```

`--all` runs every installed tool that supports the given input type. Only `u`, `e`, `p`, `d` and `url` work with `--all`. Tools that need API keys or a login are skipped unless `--include-credentialed` is passed, and tools that ask questions while they run (such as `ghunt login` or the fsociety menu) are always skipped; run those on their own. Tools that monitor a target continuously (such as `instagram-monitor`) never run under `--all` or `auto`, because they do not exit on their own.

`otinstaller auto <target>` detects whether the target is an email, domain, URL or username and runs every installed tool that takes that input, passing it with the tool's own flag, the same way as a typed input. It skips the same tools as `--all`, and `--include-credentialed` works the same way. `--type` overrides the detection, for example `--type phone`. IP addresses are detected, but no tool takes an IP as a typed input yet, so `auto` reports that none match.

`otinstaller playbook --list` shows the playbooks that ship with otinstaller (`domain-recon` and `username-investigation`). To add your own, put YAML files in a `playbooks` folder in the directory you run otinstaller from; a file with the same name as a bundled playbook replaces it.

_This page mirrors the [OTinstaller README](https://github.com/OSINTVerseHQ/OTinstaller)._
