import requests
import shutil
from colorama import Fore, Style, init

init(autoreset=True)

def get_terminal_width():
    try:
        return shutil.get_terminal_size().columns
    except:
        return 80

def wrap_banner_lines(banner, width):
    wrapped = []
    for line in banner.splitlines():
        if len(line) <= width:
            wrapped.append(line)
        else:
            for i in range(0, len(line), width):
                wrapped.append(line[i:i+width])
    return '\n'.join(wrapped)

def center_text(text, width):
    return '\n'.join(line.center(width) for line in text.splitlines())

ascii_banner = r"""
 _   _ _ _   _                 _         ___________   _                     _             
| | | | | | (_)               | |       |_   _| ___ \ | |                   | |            
| | | | | |_ _ _ __ ___   __ _| |_ ___    | | | |_/ / | |     ___   ___ __ _| |_ ___  _ __ 
| | | | | __| | '_ ` _ \ / _` | __/ _ \   | | |  __/  | |    / _ \ / __/ _` | __/ _ \| '__|
| |_| | | |_| | | | | | | (_| | ||  __/  _| |_| |     | |___| (_) | (_| (_| | || (_) | |   
 \___/|_|\__|_|_| |_| |_|\__,_|\__\___|  \___/\_|     \_____/\___/ \___\__,_|\__\___/|_|   
                                                                                          
                                                                                          
"""

def get_ipinfo_data(ip):
    try:
        print("\nDelving through the vast internet stratosphere to locate the IP...")
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        response.raise_for_status()
        data = response.json()
        return {
            "IP": data.get("ip"),
            "City": data.get("city"),
            "Region or State": data.get("region"),
            "Country": data.get("country"),
            "Coordinates": data.get("loc"),
            "ISP (Internet Service Provider)": data.get("org"),
            "Timezone": data.get("timezone")
        }
    except Exception as e:
        return {"error": f"Failed to get data from ipinfo.io: {str(e)}"}

def display_result(result):
    if 'error' in result:
        print(f"\n{Fore.RED}[ERROR]{Style.RESET_ALL} {result['error']}")
    else:
        print()
        for key, value in result.items():
            print(f"{Fore.RED}{key}:{Style.RESET_ALL} {value}")

def main():
    width = get_terminal_width()
    red_banner = Fore.RED + center_text(wrap_banner_lines(ascii_banner, width), width)
    credit = Fore.RED + center_text("created by dzuma youtube.com/@dzumq", width)

    print(red_banner)
    print(credit + "\n")

    ip = input("Enter IP address to geo-locate: ").strip()
    result = get_ipinfo_data(ip)
    display_result(result)

if __name__ == "__main__":
    main()

