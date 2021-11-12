import pyshark
import ipaddress
import pandas as pd
import numpy as np
from numpy import array
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt


def packet_parser(duration=100):
    capture = pyshark.LiveCapture(interface='net3',only_summaries= True)
    df = pd.DataFrame(columns = ['Time', 'UE-App', 'Length'])
    time_start = -1
    for packet in capture.sniff_continuously():
        if (packet.protocol == 'UDP' or packet.protocol == 'SIP' or packet.protocol == 'HTTP' or packet.protocol == 'TCP' or packet.protocol == 'STUN' or packet.protocol == 'DTLSv1.2') and (ipaddress.ip_address(packet.destination) in ipaddress.ip_network('192.168.20.0/24') or ipaddress.ip_address(packet.source) in ipaddress.ip_network('192.168.20.0/24')) and (ipaddress.ip_address(packet.destination) in ipaddress.ip_network('192.168.3.0/24') or ipaddress.ip_address(packet.source) in ipaddress.ip_network('192.168.3.0/24')):
                if time_start == -1:
                    time_start = packet.time
                time_end = packet.time
                if time_end - time_start < duration:
                    if packet.source == '192.168.3.101' or packet.destination == '192.168.3.101' :
                        app = 'web-rtc'
                    if packet.source == '192.168.3.102' or packet.destination == '192.168.3.102' :
                        app = 'sipp'
                    if packet.source == '192.168.3.103' or packet.destination == '192.168.3.103' :
                        app = 'web-server'
                    if packet.source == '192.168.20.2' or packet.destination == '192.168.20.2' :
                        ue = 'UE1'
                    if packet.source == '192.168.20.3' or packet.destination == '192.168.20.3' :
                        ue = 'UE2'
                    if packet.source == '192.168.20.4' or packet.destination == '192.168.20.4' :
                        ue = 'UE3'    
                    time = packet.time            
                    ue_app = str(ue) + ": " + str(app)        
                    length = packet.length
                    data = {'Time': time, 'UE-App':ue_app, 'Length':length}
                    temp_df = pd.DataFrame.from_dict(data)
                    new_df = new_df.append(temp_df, ignore_index=True)
    return new_df                


def make_mini_windows(new_df, offset = 0,duration=1):

    '''Finds the beggining indexes for each window'''
    X_dict = { }
    X_dict['UE1'] = {}
    X_dict['UE1']['web-rtc'] = []
    X_dict['UE1']['sipp'] = []
    X_dict['UE1']['web-server'] = []
    X_dict['UE2'] = {}
    X_dict['UE2']['web-rtc'] = []
    X_dict['UE2']['sipp'] = []
    X_dict['UE2']['web-server'] = []
    X_dict['UE3'] = {}
    X_dict['UE3']['web-rtc'] = []
    X_dict['UE3']['sipp'] = []
    X_dict['UE3']['web-server'] = []
    
    time_start = -1 
    for i, row in new_df.iloc[offset:,:].iterrows():

        if time_start == -1:
            time_start = row['Time']
            index_start = i

        time_end = row['Time']

        # check elapsed time
        if time_end - time_start >= duration:
            time_start = -1
            index_end = i

            # crop window
            window = new_df.iloc[index_start:index_end+1,:]
            
            length_sum = dict(window.groupby('UE-App')['Length'].sum())
            window_combs = list(window['UE-App'].unique())


            for key, value in X_dict.items():
                for j in list(X_dict[key].keys()):
                    comb = str(key) + ": " + str(j)
                    if comb in window_combs:
                        X_dict[key][str(j)].append(length_sum[comb])
                    else:
                        X_dict[key][str(j)].append(0) 
    return X_dict


def extract_x(X_dict, window=4,y_window=2):
    X = { }
    X['UE1'] = {}
    X['UE1']['web-rtc'] = []
    X['UE1']['sipp'] = []
    X['UE1']['web-server'] = []
    X['UE2'] = {}
    X['UE2']['web-rtc'] = []
    X['UE2']['sipp'] = []
    X['UE2']['web-server'] = []
    X['UE3'] = {}
    X['UE3']['web-rtc'] = []
    X['UE3']['sipp'] = []
    X['UE3']['web-server'] = []

    for (k,v), (k2,v2) in zip(X.items(), X_dict.items()):
                if k == k2:
                    for value in list(X_dict[k].keys()):
                        for i in range(len(X_dict[k][value])):
                            if i >= len(X_dict[k][value]) - (window-1) - y_window:
                                break
                            X[k][value].append((X_dict[k][value][i:i+window]))
    return X


def array_x(X):
    iters = len(X['UE1']['web-rtc'])
    X_list = []
    for i in range(iters):
        temp_list = []
        for ue, stats in X.items():
            for app, values in stats.items():
                temp_list.append(values[i])
        X_list.append(temp_list)
    
    return X_list    


def scale_x(X_list):
    scaler = MinMaxScaler()
    flattened = np.array(X_list).reshape(-1,1)
    rescaled = scaler.fit_transform(flattened)
    X_scaled = rescaled.reshape(16,9,4)
    return X_scaled