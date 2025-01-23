import requests
import dns.resolver
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import pyfiglet
from termcolor import colored
import argparse


def check_subdomain_dns(subdomain):
    try:
        # Resolve the subdomain using dnspython
        answers = dns.resolver.resolve(subdomain, 'A')
        return True
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.Timeout):
        return False


def check_http_status(subdomain):
    try:
        response = requests.get(f'http://{subdomain}', timeout=3)
        if response.status_code == 200:
            return True
    except requests.exceptions.RequestException:
        pass
    return False


def check_subdomain(subdomain, domain):
    full_subdomain = f'{subdomain}.{domain}'
    if check_subdomain_dns(full_subdomain):
        if check_http_status(full_subdomain):
            return full_subdomain
    return None


def display_banner():
    # Bold text for Subdress
    subdress_banner = pyfiglet.figlet_format("Subdress")
    print(colored(subdress_banner, 'green', attrs=['bold']))

    # Smaller text for Subdomain Enumerating Tool
    subtool_banner = pyfiglet.figlet_format("Subdomain Enumerating Tool", font="small")
    print(subtool_banner)


def main():
    parser = argparse.ArgumentParser(description="Subdomain Enumerating Tool")
    parser.add_argument("domain", help="The domain to scan for subdomains")
    args = parser.parse_args()

    subdomains = []
    domain = args.domain
    wordlist_file = 'subdword.txt'  # Use the provided wordlist file

    display_banner()

    with open(wordlist_file, 'r') as file:
        file_content = file.readlines()
        total_words = len(file_content)

        with tqdm(total=total_words, desc="Scanning subdomains", unit="subdomain") as pbar:
            with ThreadPoolExecutor(max_workers=10) as executor:
                futures = [executor.submit(check_subdomain, i.strip(), domain) for i in file_content]

                for future in as_completed(futures):
                    result = future.result()
                    if result:
                        subdomains.append(result)
                        print(f"Valid and reachable subdomain: {result}")
                        # Append the valid subdomain to the file
                        with open('found_subdomains.txt', 'a') as outfile:
                            outfile.write(result + '\n')
                    pbar.update(1)  # Update the progress bar

    display_banner()

    print(f"Found subdomains with HTTP 200 response: {subdomains}")


if __name__ == "__main__":
    main()
