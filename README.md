# Awesome-Resolver 🛡️

A live, automatically tested, and updated list of public DNS servers.

This repository tests the uptime, speed, and filtering capabilities (ad-blocking / malware-blocking) of various public DNS servers every 12 hours and publishes the results.

Last Updated: `2025-11-07 21:10:06 UTC`

## 📊 Live DNS Status Table

| Server | Type | Address | Status | Speed (ms) | Ad-Block | Malware-Block |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |

| Cloudflare (Varsayılan) | `standard` | `1.1.1.1` | ✅ Up | 3 | ➖ No | ➖ No |
| Cloudflare (Zararlı Yazılım Engelleme) | `filtering` | `1.1.1.2` | ✅ Up | 3 | ➖ No | ☣️ Yes |
| Google (Varsayılan) | `standard` | `8.8.8.8` | ✅ Up | 17 | ➖ No | ➖ No |
| Quad9 (Zararlı Yazılım Engelleme) | `filtering` | `9.9.9.9` | ✅ Up | 20 | ➖ No | ➖ No |
| Cloudflare (DoH) | `doh` | `https://cloudflare-dns.com/dns-query` | ✅ Up | 37 | ➖ No | ➖ No |
| AdGuard DNS (Reklam Engelleme) | `filtering` | `94.140.14.14` | ✅ Up | 221 | 🛡️ Yes | ➖ No |
| AdGuard DNS (DoH) | `doh` | `https://dns.adguard-dns.com/dns-query` | ❌ Down | - | ➖ No | ➖ No |

## 📁 Filtered Lists

Raw lists of servers that are currently up and have passed the tests. These are ideal for use in Pi-hole, AdGuard Home, or other router/client configurations.

* **All "Up" Servers (JSON):** [`dns-all-up.json`](dns-all-up.json)
* **Ad-Blocking Servers (TXT):** [`dns-adblock.txt`](dns-adblock.txt)
* **Malware-Blocking Servers (TXT):** [`dns-malware-block.txt`](dns-malware-block.txt)
* **"Up" DoH Endpoints (JSON):** [`dns-doh-up.json`](dns-doh-up.json)
