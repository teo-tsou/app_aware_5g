import pyshark
import ipaddress
import pandas as pd
import numpy as np
from numpy import array
# from keras.models import Sequential
# from keras.layers import LSTM
# from keras.layers import Dense
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import time


def packet_parser(mini_window_duration=1, max_mws=2, mode=0, verbose=0, file_name="mini-windows.csv"):
    """
    This function is used to sniff continuously an interface. By using a timer, it creates mini-windows on a specific time interval
    (mini_window_duration).

    It keeps the mini-windows to a structure. When their number reaches a maximum threshold, it drops the oldest mini-window in order 
    to append the newest one.

    When the number of mini-windows stored becomes equal to the maximum number of mini-windows (max_mws), it process them as a 
    X_window and begins predictions.

    This script runs on two modes.
            a) Data Collection (mode=0):
                    This mode creates an output file to save all mini-windows found. Later we use this file for training. 

            b) Experiment (mode=1):
                    This mode creates predictions and policy slices by sensing and analyzing the channel.

    Params:
    - mini_window_duration:  Time interval of a mini-window.

    - max_mws: Number of mini-windows needed to make predictions.

    - mode: Data Collection (mode=0), Experiment (mode=1)

    - verbose: if set to 1, it prints algorithms logs to console.

    - file_name: Name of output file to store mini-windows.
    """

    # init mini windows dict structure
    mw_dict = { }
    mw_dict['UE1'] = {}
    mw_dict['UE1']['web-rtc'] = []
    mw_dict['UE1']['sipp'] = []
    mw_dict['UE1']['web-server'] = []
    mw_dict['UE2'] = {}
    mw_dict['UE2']['web-rtc'] = []
    mw_dict['UE2']['sipp'] = []
    mw_dict['UE2']['web-server'] = []
    mw_dict['UE3'] = {}
    mw_dict['UE3']['web-rtc'] = []
    mw_dict['UE3']['sipp'] = []
    mw_dict['UE3']['web-server'] = []

    # init counter of mini-windows
    mw_num = 0
    

    # init the capture
    ## uncomment below line and comment the FIleCapture, when you finish script development and want to use it on an interface.
    #capture = pyshark.LiveCapture(interface='net3',only_summaries= True)
    capture = pyshark.FileCapture('traffic.pcap',only_summaries= True)

    # init dataframe for mini-window
    mini_window_df = pd.DataFrame(columns = ['Time', 'UE-App', 'Length'])

    # siple counter to count packets if needed
    counter=0
    
    # start mini-window timer
    start_timer = time.time()

    # Data Collection mode: Init output file
    if mode == 0:
        f = open(file_name,'w')
        f.write("UE1: web-rtc,UE1: sipp,UE1: web-server,UE2: web-rtc,UE2: sipp,UE2: web-server,UE3: web-rtc,UE3: sipp,UE3: web-server\n")
        f.close()

    ## use below line when you finish script development and want to use it on an interface.
    #for packet in capture.sniff_continuously():
    # for every new packet
    for packet in capture:
        counter+=1

        # filter packet (Idea: you can apply filters inside LiveCapture maybe)
        if (packet.protocol == 'UDP' or packet.protocol == 'SIP' or packet.protocol == 'HTTP' or packet.protocol == 'TCP' or packet.protocol == 'STUN' or packet.protocol == 'DTLSv1.2') and (ipaddress.ip_address(packet.destination) in ipaddress.ip_network('192.168.20.0/24') or ipaddress.ip_address(packet.source) in ipaddress.ip_network('192.168.20.0/24')) and (ipaddress.ip_address(packet.destination) in ipaddress.ip_network('192.168.3.0/24') or ipaddress.ip_address(packet.source) in ipaddress.ip_network('192.168.3.0/24')):
            
            # obtain stats in the appropriate form
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
            p_time = packet.time            
            ue_app = str(ue) + ": " + str(app)        
            length = eval(packet.length)
            data = {'Time': [p_time], 'UE-App':[ue_app], 'Length':[length]}

            # append packet data to mini-window df
            temp_df = pd.DataFrame.from_dict(data)
            mini_window_df = mini_window_df.append(temp_df, ignore_index=True)
        
        # check time
        end_timer = time.time()

        # check if mini window duration passed and we are ready to analyze mini window
        if end_timer - start_timer >= mini_window_duration:
            
            if verbose:
                print("Crop Mini Window:",end_timer - start_timer)

            # re-init mini_window timer for next mini window
            start_timer = time.time()

            # ready to create mini-window data
            # if num of mini windows is already max_mws, we must drop the first mini-window
            if mw_num == max_mws:
                # drop first mini-window
                mw_dict = drop_first(mw_dict)
                
                # count mini windows
                mw_num = len(mw_dict['UE1']['web-rtc'])

            # now create and append current mini-window
            mw_dict = make_mini_window(mw_dict, mini_window_df)

            ## Data Collecting Mode: 
            # Store Mini-Window to file
            if mode == 0:
                # store in csv format
                store_mini_window(file_name,mw_dict)

            # count mini windows
            mw_num = len(mw_dict['UE1']['web-rtc'])
            
            # re-init mini-window df for next mini window
            mini_window_df = pd.DataFrame(columns = ['Time', 'UE-App', 'Length'])


            ## Experiment Mode: 
            # check if it is time to obtain X window
            if mw_num == max_mws and mode == 1:
                if verbose:
                    print("Obtain X window with {} mini-windows".format(mw_num))
                    print()

                
                # obtain X window, from all mini_windows
                # to array
                X_list = array_x(mw_dict)
                
                # scale 
                X_scaled = scale_x(X_list)
                
                # predict
                yhat = predict(X_scaled)

                # post slice
                post_slice(yhat)

            elif mw_num > max_mws:
                print("[ERROR]: Mini-windows surpassed max limit!")
                exit()    
    return           


def make_mini_window(mw_dict, window):

    '''Finds the beggining indexes for each window'''
    # crop window    
    length_sum = dict(window.groupby('UE-App')['Length'].sum())
    window_combs = list(window['UE-App'].unique())

    for key, value in mw_dict.items():
        for j in list(mw_dict[key].keys()):
            comb = str(key) + ": " + str(j)
            if comb in window_combs:
                mw_dict[key][str(j)].append(length_sum[comb])
            else:
                mw_dict[key][str(j)].append(0) 
    return mw_dict

def drop_first(mw_dict):
    for ue,stats in mw_dict.items():
        # for every ue
        for app in list(mw_dict[ue].keys()):
            # for every app 

            temp_list = mw_dict[ue][app]
            del temp_list[0]

            mw_dict[ue][app] = temp_list

    return mw_dict

def array_x(X):
    iters = len(X['UE1']['web-rtc'])
    X_list = []
    temp_list = []

    for ue, stats in X.items():
        # for every ue
        for app, values in stats.items():
            # for ever app 

            # 
            temp_list.append(values)
    X_list.append(temp_list)

    
    return X_list    


def scale_x(X_list):
    # To Do:  here we will load the scaler used in model training 
    scaler = MinMaxScaler()
    flattened = np.array(X_list).reshape(-1,1)
    rescaled = scaler.fit_transform(flattened)

    X_scaled = rescaled.reshape(1,9,2)

    return X_scaled

def predict(X_scaled):
    # To Do: Make sure we predict 1 value at a time. Reconfigure all functions needed
    #yhat = model.predict(X_scaled)
    yhat = -1

    return yhat


def post_slice(yhat):
    # make a policy based on yhat
    pass

def store_mini_window(file_name, mw_dict):
    f = open(file_name,'a')

    for ue, stats in mw_dict.items():
        # for every ue
        for app, value in stats.items():
            # for ever app
            
            value = str(value[0])
            if ue=='UE3' and app == 'web-server':
                # last packet
                f.write(value)
                f.write("\n")
            else:
                f.write(value)
                f.write(",")
        
    f.close()



if __name__ == "__main__":
    packet_parser(mini_window_duration=1, max_mws=2, mode=0, verbose=1)
