from scapy.all import sniff, conf
from scapy.layers.inet import IP

# Informing the user and getting the consent
print("This tool will capture and analyze network packets.")
print("Please ensure you have the necessary permissions to use this tool.")
consent = input("Do you agree to network packet sniffing? (Yes/No): ").strip().lower()

if consent != 'yes':
    print("Permission not granted. Exiting the program.")
    exit()

# Specify the log file for network packets
log_file = "packets.txt"

def packet_handler(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst

        with open(log_file, "a") as f:
            f.write(f"Source IP: {src_ip} -> Destination IP: {dst_ip}\n")

        print(f"Source IP: {src_ip} -> Destination IP: {dst_ip}")

print("Packet sniffing has started. Press 'Stop' in the Jupyter toolbar to stop.")
conf.L3socket  # Set the socket to Layer 3
sniff(prn=packet_handler, count=10) 
