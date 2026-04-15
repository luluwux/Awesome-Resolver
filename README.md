# Awesome-Resolver 🛡️

A live, automatically tested, and updated list of public DNS servers.

This repository tests the uptime, speed, and filtering capabilities (ad-blocking / malware-blocking) of various public DNS servers every 4 hours and publishes the results.

Last Updated: `2026-04-15 20:56:46 UTC`

## 📊 Live DNS Status Table

| Server | Type | Address | Status | Speed (ms) | Ad-Block | Malware-Block |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| Neustar | `standard` | `156.154.70.1` | ✅ | 10 | ❌ | ❌ |
| Quad9 | `filtering` | `9.9.9.9` | ✅ | 12 | ❌ | ❌ |
| Cloudflare (Family) | `filtering` | `1.1.1.3` | ✅ | 13 | ❌ | ✅ |
| Comodo Secure DNS | `filtering` | `8.26.56.26` | ✅ | 13 | ❌ | ❌ |
| Verisign (Secondary) | `standard` | `64.6.65.6` | ✅ | 14 | ❌ | ❌ |
| Cloudflare | `standard` | `1.1.1.1` | ✅ | 15 | ❌ | ❌ |
| Cloudflare (Secondary) | `standard` | `1.0.0.1` | ✅ | 15 | ❌ | ❌ |
| Verisign | `standard` | `64.6.64.6` | ✅ | 15 | ❌ | ❌ |
| Control D (Unfiltered) | `standard` | `76.76.2.0` | ✅ | 15 | ❌ | ❌ |
| Control D (Unfiltered Sec) | `standard` | `76.76.10.0` | ✅ | 15 | ❌ | ❌ |
| Cloudflare (Malware Block) | `filtering` | `1.1.1.2` | ✅ | 16 | ❌ | ✅ |
| Google (Secondary) | `standard` | `8.8.4.4` | ✅ | 16 | ❌ | ❌ |
| CleanBrowsing (Security) | `filtering` | `185.228.168.9` | ✅ | 16 | ❌ | ❌ |
| CleanBrowsing (Family) | `filtering` | `185.228.168.168` | ✅ | 16 | ❌ | ❌ |
| OpenDNS (FamilyShield) | `filtering` | `208.67.222.123` | ✅ | 21 | ❌ | ❌ |
| OpenDNS | `standard` | `208.67.222.222` | ✅ | 22 | ❌ | ❌ |
| OpenDNS (Secondary) | `standard` | `208.67.220.220` | ✅ | 23 | ❌ | ❌ |
| Google | `standard` | `8.8.8.8` | ✅ | 24 | ❌ | ❌ |
| Cloudflare (DoH) | `doh` | `https://cloudflare-dns.com/dns-query` | ✅ | 88 | ❌ | ❌ |
| NextDNS (DoH) | `doh` | `https://dns.nextdns.io/dns-query` | ✅ | 178 | ❌ | ❌ |
| Yandex.DNS | `standard` | `77.88.8.8` | ✅ | 179 | ❌ | ❌ |
| Yandex.DNS (Safe) | `filtering` | `77.88.8.7` | ✅ | 188 | ❌ | ❌ |
| AdGuard DNS | `filtering` | `94.140.14.14` | ✅ | 197 | ✅ | ❌ |
| AdGuard DNS (Family) | `filtering` | `94.140.14.15` | ✅ | 201 | ✅ | ❌ |
| DNS.WATCH | `standard` | `84.200.69.80` | ✅ | 205 | ❌ | ❌ |
| Google (DoH) | `doh` | `https://dns.google/dns-query` | ❌ | - | ❌ | ❌ |
| OpenDNS (DoH) | `doh` | `https://doh.opendns.com/dns-query` | ❌ | - | ❌ | ❌ |
| Quad9 (DoH) | `doh` | `https://dns.quad9.net/dns-query` | ❌ | - | ❌ | ❌ |
| AdGuard DNS (DoH) | `doh` | `https://dns.adguard-dns.com/dns-query` | ❌ | - | ❌ | ❌ |
| AdGuard DNS (Family DoH) | `doh` | `https://dns-family.adguard.com/dns-query` | ❌ | - | ❌ | ❌ |
| CleanBrowsing (Family DoH) | `doh` | `https://doh.cleanbrowsing.org/doh/family-filter/` | ❌ | - | ❌ | ❌ |
| CleanBrowsing (Ad-Block DoH) | `doh` | `https://doh.cleanbrowsing.org/doh/adblock-filter/` | ❌ | - | ❌ | ❌ |
| Yandex (Family DoH) | `doh` | `https://dns.yandex.com/dns-query/family/` | ❌ | - | ❌ | ❌ |
| Control D (DoH) | `doh` | `https://dns.controld.com/dns-query` | ❌ | - | ❌ | ❌ |
| ADnull (DoH) | `doh` | `https://dns.adnull.com/dns-query` | ❌ | - | ❌ | ❌ |
| Mullvad (Ad-block) | `filtering` | `193.138.218.74` | ❌ | - | ❌ | ❌ |
| Mullvad (DoH) | `doh` | `https://doh.mullvad.net/dns-query` | ❌ | - | ❌ | ❌ |
| DNS0.eu | `filtering` | `193.110.81.0` | ❌ | - | ❌ | ❌ |
| DNS0.eu (DoH) | `doh` | `https://doh.dns0.eu/` | ❌ | - | ❌ | ❌ |


## 📁 Filtered Lists

Raw lists of servers that are currently up and have passed the tests. These are ideal for use in Pi-hole, AdGuard Home, or other router/client configurations.

* **All "Up" Servers (JSON):** [`dns-all-up.json`](dns-all-up.json)
* **Ad-Blocking Servers (TXT):** [`dns-adblock.txt`](dns-adblock.txt)
* **Malware-Blocking Servers (TXT):** [`dns-malware-block.txt`](dns-malware-block.txt)
* **"Up" DoH Endpoints (JSON):** [`dns-doh-up.json`](dns-doh-up.json)
