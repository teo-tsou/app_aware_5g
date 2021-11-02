import pyshark
import ipaddress
import csv

cap = pyshark.FileCapture('traffic.pcap',only_summaries= True)

with open('traffic.csv', 'w', newline='') as traffic:
    writer = csv.writer(traffic)
    writer.writerow(["Packet_Num", "Time", "Source", "Destination", "Protocol", "Length"])
    try:
        for packet in cap:
            if (packet.protocol == 'UDP' or packet.protocol == 'SIP' or (packet.protocol == 'HTTP' and (int(packet.length) == 168 or int(packet.length) == 681 ))) and (ipaddress.ip_address(packet.destination) in ipaddress.ip_network('192.168.20.0/24') or ipaddress.ip_address(packet.source) in ipaddress.ip_network('192.168.20.0/24')):
                formattedLine = str(packet).split(" ")[0:6]
                wr = csv.writer(traffic, quoting=csv.QUOTE_ALL)
                wr.writerow(formattedLine[0:6])  
    except:    
            print("last packet")        