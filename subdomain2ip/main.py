# Written by: 4lir4d
# Date: 2025/02/05
# Description: This script is written to find the IP addresses of the subdomains 

import dns.resolver

def get_ip_addresses(domain):
    try:
        result = dns.resolver.resolve(domain, 'A') 
        ip_addresses = [str(rdata) for rdata in result]
        return ip_addresses
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        print(f"No IP address found for: {domain}")
    except dns.resolver.NoNameservers:
        print(f"Nameservers failed to answer the query for: {domain}")

def main():
    with open('subf.txt', 'r') as file:
        subdomains = file.readlines()
    
    subdomains = [subdomain.strip() for subdomain in subdomains]

    with open('subdomains_ips.txt', 'w') as output_file:
        for subdomain in subdomains:
            print(f"Fetching IP addresses for: {subdomain}")
            ip_addresses = get_ip_addresses(subdomain)
            if ip_addresses:
                for ip in ip_addresses:
                    output_file.write(f"{subdomain}: {ip}\n")
            else:
                output_file.write(f"{subdomain}: No IP address found\n") # subdomains output that I write them to the file-> subdomains_ips.txt

if __name__ == "__main__":
    main()

