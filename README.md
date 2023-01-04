## [🐝](https://keys.openpgp.org/vks/v1/by-fingerprint/E616FA7221A1613E5B99206297966C06BB06757B) [Github ](http://github.com/randymcmillan) [Twitter](https://twitter.com/RandyMcMillan) [Keybase](https://randymcmillan.keybase.pub)
<AUTOMATION>
<p>

## [![Awesome](https://awesome.re/badge.svg)](https://github.com/RandyMcMillan/randymcmillan/blob/master/sources/awesome.md) [![legit](https://github.com/RandyMcMillan/legit/actions/workflows/automate.yml/badge.svg)](https://github.com/RandyMcMillan/legit/actions/workflows/automate.yml) [![statoshi](https://github.com/bitcoincore-dev/statoshi/actions/workflows/statoshi.yml/badge.svg)](https://github.com/bitcoincore-dev/statoshi/actions/workflows/statoshi.yml)         

<CENTER></CENTER>

</p>
</AUTOMATION>

<details>
<summary>nostr NIP-05 verification</summary>
<p>

[https://nvk.org/n00b-nip](https://nvk.org/n00b-nip5)

NIP5: Mapping Nostr keys to DNS-based internet identifiers

Buy a domain

Setup Domain DNS records to point to GitHub Pages:

| Type | Host              | Answer          | TTL  | Priority |
|------|-------------------|-----------------|------|----------|
| A    | randymcmillan.net | 185.199.108.153 | 3600 |          |
| A    | randymcmillan.net | 185.199.109.153 | 3600 |          |
| A    | randymcmillan.net | 185.199.110.153 | 3600 |          |
| A    | randymcmillan.net | 185.199.111.153 | 3600 |          |

$`` dig randymcmillan.net``

![randymcmillan@randymcmillan.net](randymcmillan@randymcmillan.net.png)

Create a new github repo github.com/new

Create a new file your-repo/.well-known/nostr.json

Edit nostr.json to reflect YOUR pub key and desired nickname this content:

```json
{
  "names": {
  "randymcmillan": "e88a691e98d9987c964521dff60025f60700378a4879180dcbbb4a5027850411"
  }
}
```

Create a new file in the root folder `_config.yml`  and add this line

```
include: [".well-known"]
```

Navigate to github.com/RandyMcMillan/randmcmillan/settings/pages

Under "Build and deployment" select "Deploy from branch" then below select "Main/Master" branch

Under "Custom domain" type your naked randymcmillan.net (github might complain, ignore)

Below it, check Enforce HTTPS. Sometimes this may take a few minutes to be available.

Then head over [branle.netlify.app/settings](https://branle.netlify.app/settings) or [astral.ninja/settings](https://astral.ninja/settings) (using an extension like [Alby](https://getalby.com) or [nos2x](https://chrome.google.com/webstore/detail/nos2x/kpgefcfmnafjgpblomihpgmejjdanjjp))
edit the NIP-05 Indentifier field to reflect "randymcmillan@randymcmillan.net" and press Save
you are all set now, enjoy the vanity address.
</p>
</details>

----


<details>
<summary>legit - git commit custom hash</summary>

```shell
git clone https://github.com/RandyMcMillan/legit.git ~/legit && \
cd ~/legit && ./make-legit.sh
```
</p>
</details>
<details>
<summary>statoshi.host - dockerized bitcoin node statistics</summary>

```shell
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" && \
brew install docker docker-compose make && \
git clone https://github.com/bitcoincore-dev/statoshi.host.git ~/statoshi.host && \
cd ~/statoshi.host && make init run user=root port=80
```
</p>
</details>
<details>
<summary>docker.shell - wrap your $HOME in an alpine shell</summary>

```shell
git clone https://github.com/RandyMcMillan/docker.shell.git ~/docker.shell && \
cd docker.shell && \
make shell user=root
```
</p>
</details>

<details>
<summary>👀</summary>
<p>

```shell
seq 0 947 | (while read -r n; do bitcoin-cli gettxout \
54e48e5f5c656b26c3bca14a8c95aa583d07ebe84dde3b7dd4a78f4e4186e713 $n \
| jq -r '.scriptPubKey.asm' | awk '{ print $2 $3 $4 }'; done) | \
tr -d '\n' | cut -c 17-368600 | xxd -r -p > bitcoin.pdf
```

</p>
</details>

<details>
<summary>👀</summary>
<p>

#### Referal Links:

[![DigitalOcean Referral Badge](https://web-platforms.sfo2.digitaloceanspaces.com/WWW/Badge%202.svg)](https://www.digitalocean.com/?refcode=ae5c7d05da91&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)

</p>
</details>