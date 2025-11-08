# Awesome-Resolver 🛡️

A live, automatically tested, and updated list of public DNS servers.

This repository tests the uptime, speed, and filtering capabilities (ad-blocking / malware-blocking) of various public DNS servers every 12 hours and publishes the results.

Last Updated: `2025-11-08 18:30:27 UTC`

## 📊 Live DNS Status Table

| Server | Type | Address | Status | Speed (ms) | Ad-Block | Malware-Block |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| Quad9 | `filtering` | `9.9.9.9` | ✅ | 6 | ❌ | ❌ |
| OpenDNS | `standard` | `208.67.222.222` | ✅ | 7 | ❌ | ❌ |
| Cloudflare | `standard` | `1.1.1.1` | ✅ | 8 | ❌ | ❌ |
| Google | `standard` | `8.8.8.8` | ✅ | 8 | ❌ | ❌ |
| Cloudflare (Malware Block) | `filtering` | `1.1.1.2` | ✅ | 8 | ❌ | ✅ |
| Cloudflare (Family) | `filtering` | `1.1.1.3` | ✅ | 8 | ❌ | ✅ |
| OpenDNS (FamilyShield) | `filtering` | `208.67.222.123` | ✅ | 10 | ❌ | ❌ |
| Neustar | `standard` | `156.154.70.1` | ✅ | 11 | ❌ | ❌ |
| CleanBrowsing (Security) | `filtering` | `185.228.168.9` | ✅ | 11 | ❌ | ❌ |
| CleanBrowsing (Family) | `filtering` | `185.228.168.168` | ✅ | 12 | ❌ | ❌ |
| Cloudflare (DoH) | `doh` | `https://cloudflare-dns.com/dns-query` | ✅ | 54 | ❌ | ❌ |
| DNS.WATCH | `standard` | `84.200.69.80` | ✅ | 88 | ❌ | ❌ |
| Yandex.DNS | `standard` | `77.88.8.8` | ✅ | 128 | ❌ | ❌ |
| Yandex.DNS (Safe) | `filtering` | `77.88.8.7` | ✅ | 135 | ❌ | ❌ |
| AdGuard DNS (Family) | `filtering` | `94.140.14.15` | ✅ | 215 | ✅ | ❌ |
| AdGuard DNS | `filtering` | `94.140.14.14` | ✅ | 219 | ✅ | ❌ |
| Comodo Secure DNS | `filtering` | `8.26.56.26` | ✅ | 372 | ❌ | ❌ |
| Digitalcourage | `standard` | `46.182.19.48` | ✅ | 1264 | ❌ | ❌ |
| LibreDNS | `standard` | `116.202.176.26` | ❌ | - | ❌ | ❌ |
| UncensoredDNS | `standard` | `91.239.100.100` | ❌ | - | ❌ | ❌ |
| Freenom | `standard` | `80.80.80.80` | ❌ | - | ❌ | ❌ |
| Google (DoH) | `doh` | `https://dns.google/dns-query` | ❌ | - | ❌ | ❌ |
| Quad9 (DoH) | `doh` | `https://dns.quad9.net/dns-query` | ❌ | - | ❌ | ❌ |
| AdGuard DNS (DoH) | `doh` | `https://dns.adguard-dns.com/dns-query` | ❌ | - | ❌ | ❌ |
| AdGuard DNS (Family DoH) | `doh` | `https://dns-family.adguard.com/dns-query` | ❌ | - | ❌ | ❌ |
| OpenDNS (DoH) | `doh` | `https://doh.opendns.com/dns-query` | ❌ | - | ❌ | ❌ |
| CleanBrowsing (Family DoH) | `doh` | `https://doh.cleanbrowsing.org/doh/family-filter/` | ❌ | - | ❌ | ❌ |
| CleanBrowsing (Ad-Block DoH) | `doh` | `https://doh.cleanbrowsing.org/doh/adblock-filter/` | ❌ | - | ❌ | ❌ |
| LibreDNS (DoH) | `doh` | `https://doh.libredns.gr/dns-query` | ❌ | - | ❌ | ❌ |
| Yandex (Family DoH) | `doh` | `https://dns.yandex.com/dns-query/family/` | ❌ | - | ❌ | ❌ |


## 📁 Filtered Lists

Raw lists of servers that are currently up and have passed the tests. These are ideal for use in Pi-hole, AdGuard Home, or other router/client configurations.

* **All "Up" Servers (JSON):** [`dns-all-up.json`](dns-all-up.json)
* **Ad-Blocking Servers (TXT):** [`dns-adblock.txt`](dns-adblock.txt)
* **Malware-Blocking Servers (TXT):** [`dns-malware-block.txt`](dns-malware-block.txt)
* **"Up" DoH Endpoints (JSON):** [`dns-doh-up.json`](dns-doh-up.json)
