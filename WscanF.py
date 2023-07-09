import subprocess
import datetime

def scan_wifi_networks():
    # Execute the command to scan for available Wi-Fi networks
    command = "nmcli -f SSID,BSSID,MODE,CHAN,FREQ,SIGNAL device wifi list"
    output = subprocess.check_output(command, shell=True, text=True)
    return output

def get_detailed_info(bssid):
    # Get detailed information for a specific Wi-Fi network based on its BSSID
    command = f"nmcli -f BSSID,ACTIVE,SSID,BARS,SECURITY,IN-USE,IP4.ADDRESS device wifi show {bssid}"
    output = subprocess.check_output(command, shell=True, text=True)
    return output

def get_ip_address():
    # Get the public IP address of the device
    command = "curl -s ifconfig.me"
    output = subprocess.check_output(command, shell=True, text=True)
    return output.strip()

def perform_nmap_scan(target, scan_type):
    # Perform an Nmap scan on the target using the specified scan type
    command = f"nmap {scan_type} {target}"
    output = subprocess.check_output(command, shell=True, text=True)
    return output

def perform_aircrack_attack(target_bssid):
    # Perform an Aircrack-ng attack by capturing the handshake
    subprocess.Popen(["airodump-ng", "--bssid", target_bssid, "-w", target_bssid, "wlan0"])

def save_to_file(filename, content):
    # Save content to a file
    with open(filename, "a") as file:
        file.write(content + "\n")

def main():
    print("Starting wireless network scanning...")
    wifi_networks = scan_wifi_networks()
    print("Found Wi-Fi networks:\n")
    print(wifi_networks)

    bssid = input("Enter the BSSID of the network you want to see detailed information for: ")
    detailed_info = get_detailed_info(bssid)
    print(f"\nDetailed information for {bssid} network:\n")
    print(detailed_info)

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip_address = get_ip_address()

    save_to_file("network.txt", wifi_networks)
    save_to_file("log.txt", f"{current_time} - IP address: {ip_address}")

    target = input("Enter the target for Nmap scan (IP address or domain name): ")
    print("\nAvailable Nmap scan options:")
    print("1. OS scan: Provides information about the target system's operating system.")
    print("2. Regular scan: Performs a standard port scan.")
    print("3. Quick scan: Performs a fast port scan.")
    print("4. Slow scan: Performs a slow comprehensive scan.")
    scan_type = input("Select the Nmap scan option to use (1-4): ")

    if scan_type == "1":
        scan_type = "-O"
    elif scan_type == "2":
        scan_type = "-T4"
    elif scan_type == "3":
        scan_type = "-T4 -F"
    elif scan_type == "4":
        scan_type = "-T1"
    else:
        print("Invalid choice. Exiting the program.")
        return

    nmap_result = perform_nmap_scan(target, scan_type)
    save_to_file("nmap.txt", nmap_result)

    attack_option = input("Do you want to perform a network attack? (Y/N): ")
    if attack_option.upper() == "Y":
        target_bssid = input("Enter the BSSID of the network to attack: ")
        perform_aircrack_attack(target_bssid)

        handshake_captured = False

        while not handshake_captured:
            print("\nWaiting for a handshake capture on the network...")
            print("Once the handshake is captured, it will be automatically saved as a .pcap file.")

            # Continuously check the captured handshake using airodump-ng
            command = f"timeout 5 aircrack-ng -w {target_bssid}-01.cap"
            output = subprocess.check_output(command, shell=True, text=True)
            if "1 handshake" in output:
                print("\nHandshake captured!")
                pcap_filename = f"{bssid}.pcap"
                subprocess.Popen(["mv", f"{target_bssid}-01.cap", pcap_filename])
                save_to_file(f"{pcap_filename} file created: {datetime.datetime.now()}")
                handshake_captured = True

if __name__ == "__main__":
    main()
