import pyshark
import ipaddress
import csv

cap1 = pyshark.FileCapture('web-rtc.pcap',only_summaries= True)
cap2 = pyshark.FileCapture('sipp.pcap',only_summaries= True)
cap3 = pyshark.FileCapture('web-server.pcap',only_summaries= True)

with open('web-rtc.csv', 'w', newline='') as web_rtc:
    writer = csv.writer(web_rtc)
    writer.writerow(["Packet_Num", "Time", "Source", "Destination", "Protocol"])
    for packet in cap1:
        if packet.protocol == 'UDP' and (ipaddress.ip_address(packet.destination) in ipaddress.ip_network('192.168.20.0/24') or ipaddress.ip_address(packet.source) in ipaddress.ip_network('192.168.20.0/24')):
            formattedLine = str(packet).split(" ")[0:5]
            wr = csv.writer(web_rtc, quoting=csv.QUOTE_ALL)
            wr.writerow(formattedLine[0:5])

with open('sipp.csv', 'w', newline='') as sipp:
    writer = csv.writer(sipp)
    writer.writerow(["Packet_Num", "Time", "Source", "Destination", "Protocol"])
    for packet in cap2:
        if packet.protocol == 'SIP' and (ipaddress.ip_address(packet.destination) in ipaddress.ip_network('192.168.20.0/24') or ipaddress.ip_address(packet.source) in ipaddress.ip_network('192.168.20.0/24')):
            formattedLine = str(packet).split(" ")[0:5]
            wr = csv.writer(sipp, quoting=csv.QUOTE_ALL)
            wr.writerow(formattedLine[0:5])

with open('web-server.csv', 'w', newline='') as server:
    writer = csv.writer(server)
    writer.writerow(["Packet_Num", "Time", "Source", "Destination", "Protocol"])
    for packet in cap3:
        if (packet.protocol == 'HTTP' or packet.protocol == 'TCP') and (ipaddress.ip_address(packet.destination) in ipaddress.ip_network('192.168.20.0/24') or ipaddress.ip_address(packet.source) in ipaddress.ip_network('192.168.20.0/24')):
            formattedLine = str(packet).split(" ")[0:5]
            wr = csv.writer(server, quoting=csv.QUOTE_ALL)
            wr.writerow(formattedLine[0:5])            


