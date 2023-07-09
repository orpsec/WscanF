# WscanF Network wifi scanner, network attacker and handshake flag bruteforce

When you run the program, it will automatically start scanning for wireless networks and display a list of the found networks.

Select and enter the BSSID of the network for which you want to view detailed information.

The program will display the detailed information of the selected network.

Next, the program will retrieve your public IP address and save it to the log.txt file.

The program will ask you to enter a target IP address or domain name to perform an Nmap scan.

It will show the available Nmap scan options and prompt you to make a selection (choose a number from 1 to 6).

The program will perform the selected Nmap scan based on your choice and save the results to the nmap.txt file.

It will ask if you want to perform a network attack (Y/N). If you choose "Y" to proceed, otherwise the program will terminate.

Enter the BSSID of the network you want to launch the attack on.

The program will initiate the airodump-ng tool to capture handshakes on the network.

Once a handshake is captured, it will be automatically saved as a .pcap file with the BSSID as the filename.

The program will present attack options. Select the desired attack by choosing a number (1 to 4).

The program will execute the chosen attack.
