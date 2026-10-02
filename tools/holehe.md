# Holehe

holehe allows you to check if the mail is used on different sites like twitter, instagram and will retrieve information on sites with the forgotten password function.

## Source

- Repository: https://github.com/megadose/holehe
- License: GPL-3.0

## Install

```bash
otinstaller install holehe
```

otinstaller installs the pip package `holehe` pinned to version `1.61` in a dedicated virtualenv.

## Credentials

No API keys needed.

## Input types

| Input | Typed input | Tool arguments |
| --- | --- | --- |
| email (`e`) | `e:example@example.com` | `example@example.com` (positional) |

## Example output

```text
example output for holehe:
------------------------------------------------------------
[+] Checking email: exampleuser@gmail.com
[+] Found 34 accounts across 120+ sites

[+] Social Media
    Twitter: https://twitter.com/exampleuser
    Instagram: https://instagram.com/exampleuser
    Facebook: https://facebook.com/exampleuser
    LinkedIn: https://linkedin.com/in/exampleuser
    Snapchat: https://snapchat.com/add/exampleuser
    TikTok: https://tiktok.com/@exampleuser
    Pinterest: https://pinterest.com/exampleuser

[+] Professional
    GitHub: https://github.com/exampleuser
    LinkedIn: https://linkedin.com/in/exampleuser
    StackOverflow: https://stackoverflow.com/users/12345/exampleuser
    Medium: https://medium.com/@exampleuser
    Dev.to: https://dev.to/exampleuser

[+] Shopping & Services
    Amazon: https://amazon.com/exampleuser
    eBay: https://ebay.com/usr/exampleuser
    PayPal: https://paypal.com/exampleuser
    Stripe: https://stripe.com/exampleuser
    Shopify: https://exampleuser.myshopify.com

[+] Developer Platforms
    GitHub: https://github.com/exampleuser
    GitLab: https://gitlab.com/exampleuser
    Bitbucket: https://bitbucket.org/exampleuser
    Docker Hub: https://hub.docker.com/u/exampleuser
    npm: https://npmjs.com/~exampleuser
    PyPI: https://pypi.org/user/exampleuser

[+] Developer Tools
    StackOverflow: https://stackoverflow.com/users/12345/exampleuser
    Dev.to: https://dev.to/exampleuser
    Hashnode: https://hashnode.com/@exampleuser
    CodePen: https://codepen.io/exampleuser
    Replit: https://replit.com/@exampleuser
    CodeSandbox: https://codesandbox.io/u/exampleuser

[+] Forums & Communities
    Reddit: https://reddit.com/user/exampleuser
    Hacker News: https://news.ycombinator.com/user?id=exampleuser
    Product Hunt: https://producthunt.com/@exampleuser
    Indie Hackers: https://indiehackers.com/exampleuser

------------------------------------------------------------
(Example truncated - real output contains 34 sites found across 120+ sites checked)
```

## Run

Plain arguments after `--` are passed to the tool unchanged:

```bash
otinstaller run holehe -- example@example.com
```

Typed inputs are mapped to this tool's flags:

```bash
otinstaller run holehe e:example@example.com
```

Results are saved to `./results/holehe/<target>/`.
