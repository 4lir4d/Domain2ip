import socket
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, init, Style

# Initialize Colorama for colored output
init(autoreset=True)

def create_file_if_not_exists(filename):
    """Create a file if it does not exist."""
    try:
        open(filename, 'a').close()
    except Exception as error:
        print(f"Error creating file: {error}")

def is_ip_logged(ip_address, filename):
    """Check if an IP address is already logged in the file."""
    try:
        with open(filename, 'r') as file:
            return ip_address in file.read()
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return False

def log_ip(ip_address, filename):
    """Log the IP address to the file."""
    try:
        with open(filename, 'a') as file:
            file.write(ip_address + '\n')
    except Exception as error:
        print(f"Error writing to file {filename}: {error}")

def fetch_ip_address(domain):
    """Fetch and log the IP address of a given domain."""
    try:
        ip_address = socket.gethostbyname(domain)
        if not is_ip_logged(ip_address, 'ips.txt'):
            print(f"Retrieved IP: {Fore.YELLOW}{Style.BRIGHT}{ip_address}")
            log_ip(ip_address, 'ips.txt')
    except socket.gaierror:
        print(f"Failed to resolve domain: {domain}")
    except Exception as error:
        print(f"Error processing domain {domain}: {error}")

def read_domains_from_file(filename):
    """Read domains from a specified file."""
    try:
        with open(filename, 'r') as file:
            return [line.strip().replace('http://', '').replace('https://', '') for line in file]
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []
    except Exception as error:
        print(f"Error reading from file {filename}: {error}")
        return []

def run():
    """Main function to execute domain-to-IP conversion."""
    print(f"{Fore.YELLOW}{Style.BRIGHT}DOMAIN TO IP CONVERTER")

    # Create ips.txt if it does not exist
    create_file_if_not_exists('ips.txt')

    # Get the input file name from the user
    input_filename = input(f"{Fore.RED}{Style.BRIGHT}Enter the domain list filename: ")
    domains = read_domains_from_file(input_filename)

    if not domains:
        print("No domains to process. Exiting.")
        return

    # Get the number of threads from the user
    try:
        max_threads = int(input(f"{Fore.WHITE}Enter number of threads: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for threads.")
        return

    # Execute IP resolution with the specified number of threads
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        executor.map(fetch_ip_address, domains)

if __name__ == "__main__":
    run()

