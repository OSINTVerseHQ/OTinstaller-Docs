# theHarvester

Find emails, subdomains and names for a domain

## Source

- Repository: https://github.com/laramies/theHarvester
- License: not stated

## Install

```bash
otinstaller install theharvester
```

otinstaller clones `https://github.com/laramies/theHarvester.git` at ref `4.11.1` into a dedicated virtualenv, then installs the clone itself as a package.

## Credentials

Optional keys: `SHODAN_API_KEY`, `HUNTER_API_KEY`.

Keys are stored in `~/.otinstaller/.env`, one `KEY=value` per line. This tool only receives the keys listed above.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| domain (`d`) | `d:example.com` | `--domain example.com` |
| email (`e`) | `e:example@example.com` | `--email example@example.com` |

## Example output

```text
example output for theharvester:
------------------------------------------------------------
[*] Target: example.com
[*] Searching sources: google, bing, bingapi, duckduckgo, yahoo, duckduckgohtml, dogpile, twitter, linkedin, github, crtsh, certspotter, threatcrowd, virustotal, threatminer, otx, alienvault, rapiddns, sublist3r, bufferover, hackertarget, anubis, amass, dnsdumpster, urlscan, netcraft, wayback, commoncrawl, robtex, securitytrails, censys, certspotter, fofa, hunter, zoomeye, shodan, censys, binaryedge, greynoise, passive

[*] Emails found (12):
    admin@example.com
    contact@example.com
    support@example.com
    info@example.com
    sales@example.com
    marketing@example.com
    hr@example.com
    jobs@example.com
    security@example.com
    abuse@example.com
    webmaster@example.com
    postmaster@example.com

[*] Hosts found (24):
    example.com
    www.example.com
    mail.example.com
    ftp.example.com
    smtp.example.com
    pop.example.com
    imap.example.com
    webmail.example.com
    vpn.example.com
    remote.example.com
    dev.example.com
    staging.example.com
    test.example.com
    api.example.com
    blog.example.com
    shop.example.com
    docs.example.com
    help.example.com
    forum.example.com
    community.example.com
    status.example.com
    cdn.example.com
    static.example.com
    assets.example.com

[*] IPs found (8):
    192.0.2.1
    192.0.2.2
    192.0.2.3
    198.51.100.1
    198.51.100.2
    198.51.100.3
    203.0.113.1
    203.0.113.2

[*] ASNs found (3):
    AS15169 (Google LLC)
    AS13335 (Cloudflare, Inc.)
    AS16509 (Amazon.com, Inc.)

------------------------------------------------------------
(Example truncated - real output contains more emails, hosts, and IPs)
```

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run theharvester -- --domain example.com --email example@example.com
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run theharvester d:example.com e:example@example.com
```

Results are saved to `./results/theharvester/<target>/`.
