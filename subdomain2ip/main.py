# Written by: 4lir4d
# Date: 2025/02/05
# Description: This script is written to find the IP addresses of the subdomains 

import dns.resolver
import argparse
import requests

def get_ip_addresses(domain):
    try:
        result = dns.resolver.resolve(domain, 'A') 
        ip_addresses = [str(rdata) for rdata in result]
        return ip_addresses
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        print(f"No IP address found for: {domain}")
    except dns.resolver.NoNameservers:
        print(f"Nameservers failed to answer the query for: {domain}")

def is_alive(domain):
    try:
        response = requests.get(f"http://{domain}", timeout=5)
        if response.status_code in [200, 301, 302, 403, 401, 405, 500, 503, 429, 400, 404, 502]:
            return True
    except requests.RequestException:
        pass
    return False

def main():
    parser = argparse.ArgumentParser(description="Find IP addresses of subdomains")
    parser.add_argument('-f', '--file', type=str, required=True, help="Input file containing subdomains")
    parser.add_argument('-l', '--live', action='store_true', help="Write alive subdomains to live_subdomains.txt")
    args = parser.parse_args()

    with open(args.file, 'r') as file:
        subdomains = file.readlines()
    
    subdomains = [subdomain.strip() for subdomain in subdomains]

    with open('subdomains_ips.txt', 'w') as output_file:
        if args.live:
            live_subdomains = open('live_subdomains.txt', 'w')
        
        for subdomain in subdomains:
            print(f"Fetching IP addresses for: {subdomain}")
            ip_addresses = get_ip_addresses(subdomain)
            if ip_addresses:
                for ip in ip_addresses:
                    output_file.write(f"{subdomain}: {ip}\n")
                if args.live and is_alive(subdomain):
                    live_subdomains.write(f"{subdomain}\n")
            else:
                output_file.write(f"{subdomain}: No IP address found\n")
        
        if args.live:
            live_subdomains.close()

if __name__ == "__main__":
    main()

