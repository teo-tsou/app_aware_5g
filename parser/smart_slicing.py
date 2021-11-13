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
import time


def packet_parser(mini_window_duration=1, max_mws, first_pred_offset=1):
    """
    This funtion sniffs and stored continously the filtered packets. 
    When the time come it starts predicting on a standard time interval.
    It finds the X window by searching back in time from the current time until the window_duration passes in the new_df. 

    Params:
    - window_duration:  Time duration of a X window, that will be used for preditions.

    - prediction_interval: Time duration of how often we will make predictions.

    - first_pred_offset: Time duration to wait until the first prediction. We wait to collect enough data for X window.
    """

    # mini windows dict
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


    mw_num = 0

    capture = pyshark.LiveCapture(interface='net3',only_summaries= True)
    mini_window_df = pd.DataFrame(columns = ['Time', 'UE-App', 'Length'])
    mw_time_start = -1
    for packet in capture.sniff_continuously():
        if (packet.protocol == 'UDP' or packet.protocol == 'SIP' or packet.protocol == 'HTTP' or packet.protocol == 'TCP' or packet.protocol == 'STUN' or packet.protocol == 'DTLSv1.2') and (ipaddress.ip_address(packet.destination) in ipaddress.ip_network('192.168.20.0/24') or ipaddress.ip_address(packet.source) in ipaddress.ip_network('192.168.20.0/24')) and (ipaddress.ip_address(packet.destination) in ipaddress.ip_network('192.168.3.0/24') or ipaddress.ip_address(packet.source) in ipaddress.ip_network('192.168.3.0/24')):
            
            # append to mini-window df every filtered packet
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
            mini_window_df = mini_window_df.append(temp_df, ignore_index=True)

            # for first time set time of first packet
            if mw_time_start == -1:
                mw_time_start = time
        
            # check time
            mw_time_end = packet.time

            # check if mini window duration passed and we are ready to analyze mini window
            if mw_time_end - mw_time_start >= mini_window_duration and mw_time_start != -1:
                
                # re-init mini_window timer for next mini window
                mw_time_start = -1

                # ready to create mini-window data
                # if num of mini windows is already max_mws, we must drop the first mini-window
                if mw_num == max_mws:
                    # drop first mini-window
                    mw_dict = drop_first(mw_dict)
                    
                    # count mini windows
                    mw_num = len(mw_dict['UE1']['web-rtc'])

                # now create and append current mini-window
                mw_dict = make_mini_window(mw_dict, window)
                mw_num = mw_num = len(mw_dict['UE1']['web-rtc'])
                
                # re-init mini-window df for next mini window
                mini_window_df = pd.DataFrame(columns = ['Time', 'UE-App', 'Length'])



            # check if it is time to obtain X window
            if mw_num == max_mws:
                
                # obtain X window, from all mini_windows
                X = mw_dict

                # to array
                X_list = array_x(X)

                # scale 
                X_scaled = scale_x(X_list)

                # predict
                yhat = predict(X_scaled)

                # post slice
                post_slice(yhat)

            elif mw_num > max_mws:
                print("[ERROR]: Mini-windows surpassed max limit!")
                exit()
                

    return mini_window_df                


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

            temp_list = mw_dict[ue][app])
            del temp_list[0]

            mw_dict[ue][app] = temp_list

    return mw_dict

def extract_x(X, mw_dict):
    for (k,v), (k2,v2) in zip(X.items(), mw_dict.items()):
        # for every ue
        if k == k2:
            # for every app
            for value in list(mw_dict[k].keys()):
                X[k][value].append(mw_dict[k][value])
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
    # To Do:  here we will load the scaler used in model training 
    scaler = MinMaxScaler()
    flattened = np.array(X_list).reshape(-1,1)
    rescaled = scaler.fit_transform(flattened)
    X_scaled = rescaled.reshape(16,9,4)
    return X_scaled

def predict(X_scaled):
    # To Do: Make sure we predict 1 value at a time. Reconfigure all functions needed
    yhat = model.predict(X_scaled[0].reshape(1,9,4))


    return yhat


def post_slice(yhat):
    # make a policy based on yhat
    pass