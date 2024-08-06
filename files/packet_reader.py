from scapy.all import rdpcap , Raw
import sys

def print_packet_data(pcap_file):
    packets = rdpcap(pcap_file)
    for packet in packets:
        print(packet.summary())
        if Raw in packet:
            print(f"Raw Data: {bytes(packet[Raw])}\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python print_pcap_data.py <pcapng_file>")
        sys.exit(1)
    
    pcap_file = sys.argv[1]
    print_packet_data(pcap_file)
