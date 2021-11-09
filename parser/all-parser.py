import pyshark
import ipaddress
import csv

cap = pyshark.FileCapture('traffic.pcap',only_summaries= True,  include_raw=False)

with open('all-traffic.csv', 'w', newline='') as traffic:
    writer = csv.writer(traffic)
    writer.writerow(["Packet_Num", "Time", "Source", "Destination", "Protocol", "Length"])
    for packet in cap:
       if (packet.protocol == 'UDP' or packet.protocol == 'SIP' or packet.protocol == 'HTTP' or packet.protocol == 'TCP' or packet.protocol == 'STUN' or packet.protocol == 'DTLSv1.2') and (ipaddress.ip_address(packet.destination) in ipaddress.ip_network('192.168.20.0/24') or ipaddress.ip_address(packet.source) in ipaddress.ip_network('192.168.20.0/24')) and (ipaddress.ip_address(packet.destination) in ipaddress.ip_network('192.168.3.0/24') or ipaddress.ip_address(packet.source) in ipaddress.ip_network('192.168.3.0/24')) :
           formattedLine = str(packet).split(" ")[0:6]
           wr = csv.writer(traffic, quoting=csv.QUOTE_ALL)
           wr.writerow(formattedLine[0:6])  
    
