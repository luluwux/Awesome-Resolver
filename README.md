`2025-11-07 20:42:07 UTC`
| Server | Type | Address | Status | Speed (ms) | Ad-Block | Malware-Block |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| Quad9 (Zararlı Yazılım Engelleme) | `filtering` | `9.9.9.9` | ✅ Up | 6 | ➖ No | ➖ No |
| Google (Varsayılan) | `standard` | `8.8.8.8` | ✅ Up | 7 | ➖ No | ➖ No |
| Cloudflare (Varsayılan) | `standard` | `1.1.1.1` | ✅ Up | 8 | ➖ No | ➖ No |
| Cloudflare (Zararlı Yazılım Engelleme) | `filtering` | `1.1.1.2` | ✅ Up | 8 | ➖ No | ☣️ Yes |
| Cloudflare (DoH) | `doh` | `https://cloudflare-dns.com/dns-query` | ✅ Up | 70 | ➖ No | ➖ No |
| AdGuard DNS (Reklam Engelleme) | `filtering` | `94.140.14.14` | ✅ Up | 216 | 🛡️ Yes | ➖ No |
| AdGuard DNS (DoH) | `doh` | `https://dns.adguard-dns.com/dns-query` | ❌ Down | - | ➖ No | ➖ No |

# DNS-List 

A live, automatically tested, and updated list of public DNS servers.

This repository tests the uptime, speed, and filtering capabilities (ad-blocking / malware-blocking) of various public DNS servers every 12 hours and publishes the results.

Last Updated: ``Waiting for the first script run...``

## 📊 Live DNS Status Table

This table will be generated when the `check_dns.py` script runs for the first time.
## 📁 Filtered Lists

Raw lists of servers that are currently up and have passed the tests. These are ideal for use in Pi-hole, AdGuard Home, or other router/client configurations.

* **All "Up" Servers (JSON):** [`dns-all-up.json`](dns-all-up.json)
* **Ad-Blocking Servers (TXT):** [`dns-adblock.txt`](dns-adblock.txt)
* **Malware-Blocking Servers (TXT):** [`dns-malware-block.txt`](dns-malware-block.txt)
* **"Up" DoH Endpoints (JSON):** [`dns-doh-up.json`](dns-doh-up.json)Kod
