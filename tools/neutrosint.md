# NeutrOSINT

Check if an email address or username exists on ProtonMail.

## Source

- Repository: https://github.com/Kr0wZ/NeutrOSINT
- License: MIT

## Install

```bash
otinstaller install neutrosint
```

otinstaller clones `https://github.com/Kr0wZ/NeutrOSINT.git` into a dedicated virtualenv, then installs the clone itself as a package.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| email (`e`) | `e:example@example.com` | `--email example@example.com` |
| username (`u`) | `u:exampleuser` | `--email exampleuser` |

## Example output

```text
example output for neutrosint:
------------------------------------------------------------
username and password not specified, using light mode...

(NeutrOSINT banner omitted)

[-] Proton email does not exist: doesnotexist9k2x@example.com

[+] Valid email: exampleuser@proton.me - PGP key creation date:
    2021-03-14T09:41:51+00:00 - Fingerprint: 1A2B3C4D5E6F7890ABCDEF1234567890ABCDEF12
    - Algorithm: rsa3072

[?] Not a protonmail address, can't determine validity: someone@gmail.com

[-] Error when requesting the API
------------------------------------------------------------
(Example trimmed - real output starts with an ASCII banner)
```

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run neutrosint -- --email example@example.com --email exampleuser
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run neutrosint e:example@example.com u:exampleuser
```

Results are saved to `./results/neutrosint/<target>/`.
