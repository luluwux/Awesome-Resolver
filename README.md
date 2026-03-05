# Awesome-Resolver 🛡️

A live, automatically tested, and updated list of public DNS servers.

This repository tests the uptime, speed, and filtering capabilities (ad-blocking / malware-blocking) of various public DNS servers every 4 hours and publishes the results.

Last Updated: `2026-03-05 08:51:23 UTC`

## 📊 Live DNS Status Table

| Server | Type | Address | Status | Speed (ms) | Ad-Block | Malware-Block |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| Verisign (Secondary) | `standard` | `64.6.65.6` | ✅ | 2 | ❌ | ❌ |
| Cloudflare (Secondary) | `standard` | `1.0.0.1` | ✅ | 3 | ❌ | ❌ |
| Cloudflare (Malware Block) | `filtering` | `1.1.1.2` | ✅ | 3 | ❌ | ✅ |
| Google (Secondary) | `standard` | `8.8.4.4` | ✅ | 3 | ❌ | ❌ |
| Quad9 | `filtering` | `9.9.9.9` | ✅ | 3 | ❌ | ❌ |
| Verisign | `standard` | `64.6.64.6` | ✅ | 3 | ❌ | ❌ |
| Control D (Unfiltered Sec) | `standard` | `76.76.10.0` | ✅ | 3 | ❌ | ❌ |
| Control D (Unfiltered) | `standard` | `76.76.2.0` | ✅ | 4 | ❌ | ❌ |
| Cloudflare | `standard` | `1.1.1.1` | ✅ | 5 | ❌ | ❌ |
| Cloudflare (Family) | `filtering` | `1.1.1.3` | ✅ | 5 | ❌ | ✅ |
| CleanBrowsing (Family) | `filtering` | `185.228.168.168` | ✅ | 8 | ❌ | ❌ |
| OpenDNS | `standard` | `208.67.222.222` | ✅ | 9 | ❌ | ❌ |
| CleanBrowsing (Security) | `filtering` | `185.228.168.9` | ✅ | 9 | ❌ | ❌ |
| Neustar | `standard` | `156.154.70.1` | ✅ | 9 | ❌ | ❌ |
| OpenDNS (Secondary) | `standard` | `208.67.220.220` | ✅ | 11 | ❌ | ❌ |
| Google | `standard` | `8.8.8.8` | ✅ | 12 | ❌ | ❌ |
| OpenDNS (FamilyShield) | `filtering` | `208.67.222.123` | ✅ | 12 | ❌ | ❌ |
| Cloudflare (DoH) | `doh` | `https://cloudflare-dns.com/dns-query` | ✅ | 41 | ❌ | ❌ |
| NextDNS (DoH) | `doh` | `https://dns.nextdns.io/dns-query` | ✅ | 43 | ❌ | ❌ |
| DNS.WATCH | `standard` | `84.200.69.80` | ✅ | 95 | ❌ | ❌ |
| Yandex.DNS | `standard` | `77.88.8.8` | ✅ | 134 | ❌ | ❌ |
| Yandex.DNS (Safe) | `filtering` | `77.88.8.7` | ✅ | 145 | ❌ | ❌ |
| AdGuard DNS (Family) | `filtering` | `94.140.14.15` | ✅ | 222 | ✅ | ❌ |
| AdGuard DNS | `filtering` | `94.140.14.14` | ✅ | 223 | ✅ | ❌ |
| Google (DoH) | `doh` | `https://dns.google/dns-query` | ❌ | - | ❌ | ❌ |
| OpenDNS (DoH) | `doh` | `https://doh.opendns.com/dns-query` | ❌ | - | ❌ | ❌ |
| Quad9 (DoH) | `doh` | `https://dns.quad9.net/dns-query` | ❌ | - | ❌ | ❌ |
| AdGuard DNS (DoH) | `doh` | `https://dns.adguard-dns.com/dns-query` | ❌ | - | ❌ | ❌ |
| AdGuard DNS (Family DoH) | `doh` | `https://dns-family.adguard.com/dns-query` | ❌ | - | ❌ | ❌ |
| CleanBrowsing (Family DoH) | `doh` | `https://doh.cleanbrowsing.org/doh/family-filter/` | ❌ | - | ❌ | ❌ |
| CleanBrowsing (Ad-Block DoH) | `doh` | `https://doh.cleanbrowsing.org/doh/adblock-filter/` | ❌ | - | ❌ | ❌ |
| Comodo Secure DNS | `filtering` | `8.26.56.26` | ❌ | - | ❌ | ❌ |
| Yandex (Family DoH) | `doh` | `https://dns.yandex.com/dns-query/family/` | ❌ | - | ❌ | ❌ |
| Control D (DoH) | `doh` | `https://dns.controld.com/dns-query` | ❌ | - | ❌ | ❌ |
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
