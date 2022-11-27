import pyshark
import mysql.connector

mydb = mysql.connector.connect(
host="mysql.default",
user="root",
password="password",
database="oai"
)

mycursor = mydb.cursor()


def packet_sniffer():

    """
    This funtion sniffs and stores in a DB continously the filtered packets. 
    """

    #capture = pyshark.LiveCapture(interface='net3',only_summaries= True, display_filter = "(tcp or udp or sip or stun or dtls ) and ((ip.src==192.168.3.0/24 and ip.dst==192.168.20.0/24) or (ip.src==192.168.20.0/24 and ip.dst==192.168.3.0/24))")
    capture = pyshark.FileCapture('traffic.pcap',only_summaries= True, display_filter = "(tcp or udp or sip or stun or dtls ) and ((ip.src==192.168.3.0/24 and ip.dst==192.168.20.0/24) or (ip.src==192.168.20.0/24 and ip.dst==192.168.3.0/24))")
    for packet in capture:
        data = str(packet).split(" ")[0:6]
        mycursor.execute("INSERT INTO oai.app_data (Packet_Num, Time_packet, Source, Destination, Protocol, Length_packet) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(data[0], data[1], str(data[2]) , str(data[3]) , str(data[4]), data[5]))
        mydb.commit()

    
if __name__ == "__main__":
    packet_sniffer()

