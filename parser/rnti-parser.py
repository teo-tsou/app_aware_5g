import json
import requests

URL = "http://192.168.18.202:9999/stats/"
rnti = []
all_ues = 0
while(1):

    if all_ues == 1:
        break

    r = requests.get(url = URL)
    data = r.json()
    
    if data['eNB_config']:
        for enb in data['eNB_config']:
            if enb['UE']:
                for ue in enb['UE']['ueConfig']:
                    rnti.append(ue['rnti'])
                if len(rnti) != 3:
                    rnti = []
                else:
                    all_ues = 1
            else:
                break              

print(rnti)
