import dns.resolver
import yaml
import json
import requests
import time
from datetime import datetime, timezone

TEST_DOMAIN_STANDARD = "google.com"
TEST_DOMAIN_AD = "doubleclick.net"
TEST_DOMAIN_MALWARE = "malware.testcategory.com"

def test_standard_dns(resolver_ip, domain):
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = [resolver_ip]
    resolver.timeout = 2
    resolver.lifetime = 2
    
    try:
        start_time = time.monotonic()
        answer = resolver.resolve(domain, 'A')
        end_time = time.monotonic()
        
        response_ms = int((end_time - start_time) * 1000)
        
        if answer:
            return "up", response_ms, list(str(a) for a in answer)
        else:
            return "down", 0, []
            
    except (dns.resolver.Timeout, dns.resolver.NoNameservers, dns.exception.DNSException):
        return "down", 0, []

def test_doh(url, domain):
    headers = {'accept': 'application/dns-json'}
    params = {'name': domain, 'type': 'A'}
    
    try:
        start_time = time.monotonic()
        response = requests.get(url, params=params, headers=headers, timeout=2)
        end_time = time.monotonic()
        
        response_ms = int((end_time - start_time) * 1000)
        
        if response.status_code == 200:
            data = response.json()
            if data.get('Status') == 0 and 'Answer' in data:
                return "up", response_ms, [a['data'] for a in data['Answer'] if a['type'] == 1]
        
        return "down", 0, []
        
    except requests.exceptions.RequestException:
        return "down", 0, []

def check_blocking(resolver_ip, domain):
    try:
        status, _, ips = test_standard_dns(resolver_ip, domain)
        if status == "up" and (not ips or ips[0] == "0.0.0.0"):
            return True
        return False
    except Exception:
        return False

def check_doh_blocking(url, domain):
    try:
        status, _, ips = test_doh(url, domain)
        if status == "up" and (not ips or ips[0] == "0.0.0.0"):
            return True
        return False
    except Exception:
        return False

def update_readme_table(readme_path, results):
    
    table_header = "| Server | Type | Address | Status | Speed (ms) | Ad-Block | Malware-Block |\n"
    table_header += "| :--- | :--- | :--- | :---: | :---: | :---: | :---: |\n"
    
    table_body = ""
    for res in sorted(results, key=lambda x: (x['status'] == 'down', x['response_ms'])):
        status_icon = "✅ Up" if res['status'] == 'up' else "❌ Down"
        ad_block_icon = "🛡️ Yes" if res.get('blocks_ads') else "➖ No"
        malware_block_icon = "☣️ Yes" if res.get('blocks_malware') else "➖ No"
        
        address = f"`{res['ip']}`" if res['type'] == 'standard' or res['type'] == 'filtering' else f"`{res['url']}`"
        
        table_body += f"| {res['name']} | `{res['type']}` | {address} | {status_icon} | {res['response_ms'] if res['status'] == 'up' else '-'} | {ad_block_icon} | {malware_block_icon} |\n"
        
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()

        table_start_tag = ""
        table_end_tag = ""
        
        start_index = content.find(table_start_tag)
        end_index = content.find(table_end_tag)
        
        if start_index != -1 and end_index != -1:
            new_content = (
                content[:start_index + len(table_start_tag)] +
                "\n" + table_header + table_body + "\n" +
                content[end_index:]
            )
        else:
            print("Error: Could not find 'DNS_TABLE_START' or 'DNS_TABLE_END' tags in README.md.")
            new_content = content

        time_start_tag = ""
        time_end_tag = ""
        
        time_start_index = new_content.find(time_start_tag)
        time_end_index = new_content.find(time_end_tag)
        
        if time_start_index != -1 and time_end_index != -1:
            now_utc = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S %Z')
            new_content = (
                new_content[:time_start_index + len(time_start_tag)] +
                f"`{now_utc}`" +
                new_content[time_end_index:]
            )
        else:
            print("Error: Could not find 'LAST_UPDATED_START' or 'LAST_UPDATED_END' tags in README.md.")

        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
    except IOError as e:
        print(f"Error reading or writing to README.md: {e}")

def main():
    try:
        with open('seed-list.yml', 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
    except IOError as e:
        print(f"Error: Could not read seed-list.yml: {e}")
        return
    except yaml.YAMLError as e:
        print(f"Error: Could not parse seed-list.yml: {e}")
        return

    results = []
    
    up_adblock = []
    up_malware_block = []
    up_doh = []
    all_up_data = []

    for server in config.get('servers', []):
        name = server.get('name')
        ip = server.get('ip')
        url = server.get('url')
        server_type = server.get('type')
        features = server.get('features', [])
        
        result_data = server.copy()
        
        if server_type == 'standard' or server_type == 'filtering':
            status, response_ms, _ = test_standard_dns(ip, TEST_DOMAIN_STANDARD)
            result_data['status'] = status
            result_data['response_ms'] = response_ms
            
            if status == 'up':
                blocks_ads = "ad-block" in features and check_blocking(ip, TEST_DOMAIN_AD)
                blocks_malware = "malware-block" in features and check_blocking(ip, TEST_DOMAIN_MALWARE)
                
                result_data['blocks_ads'] = blocks_ads
                result_data['blocks_malware'] = blocks_malware
                
                all_up_data.append(result_data)
                if blocks_ads:
                    up_adblock.append(ip)
                if blocks_malware:
                    up_malware_block.append(ip)

        elif server_type == 'doh':
            status, response_ms, _ = test_doh(url, TEST_DOMAIN_STANDARD)
            result_data['status'] = status
            result_data['response_ms'] = response_ms

            if status == 'up':
                blocks_ads = "ad-block" in features and check_doh_blocking(url, TEST_DOMAIN_AD)
                blocks_malware = "malware-block" in features and check_doh_blocking(url, TEST_DOMAIN_MALWARE)
                
                result_data['blocks_ads'] = blocks_ads
                result_data['blocks_malware'] = blocks_malware
                
                all_up_data.append(result_data)
                up_doh.append({"name": name, "url": url})
                if blocks_ads:
                    up_adblock.append(f"DoH: {url}")
                if blocks_malware:
                    up_malware_block.append(f"DoH: {url}")
        
        results.append(result_data)

    update_readme_table('README.md', results)

    with open('dns-all-up.json', 'w', encoding='utf-8') as f:
        json.dump(all_up_data, f, indent=2, ensure_ascii=False)
        
    with open('dns-doh-up.json', 'w', encoding='utf-8') as f:
        json.dump(up_doh, f, indent=2, ensure_ascii=False)

    with open('dns-adblock.txt', 'w', encoding='utf-8') as f:
        f.write("# Auto-updated list of ad-blocking DNS servers\n")
        f.write(f"# Last Updated: {datetime.now(timezone.utc).isoformat()}\n")
        for item in up_adblock:
            f.write(f"{item}\n")
            
    with open('dns-malware-block.txt', 'w', encoding='utf-8') as f:
        f.write("# Auto-updated list of malware-blocking DNS servers\n")
        f.write(f"# Last Updated: {datetime.now(timezone.utc).isoformat()}\n")
        for item in up_malware_block:
            f.write(f"{item}\n")

    print(f"DNS check complete. {len(results)} servers tested.")
    print(f"Updated README.md and generated lists for {len(all_up_data)} working servers.")

if __name__ == "__main__":
    main()