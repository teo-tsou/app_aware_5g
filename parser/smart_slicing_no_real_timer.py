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


def packet_parser(mini_window_duration=1, max_mws=2, mode=0, verbose=0, file_name="notimer_mini-windows.csv"):
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

    # Data Collection mode: Init output file
    if mode == 0:
        f = open(file_name,'w')
        f.write("UE1: web-rtc,UE1: sipp,UE1: web-server,UE2: web-rtc,UE2: sipp,UE2: web-server,UE3: web-rtc,UE3: sipp,UE3: web-server\n")
        f.close()

    mw_num = 0

    #capture = pyshark.LiveCapture(interface='net3',only_summaries= True)
    capture = pyshark.FileCapture('scenario2-traffic.pcap',only_summaries= True)
    mini_window_df = pd.DataFrame(columns = ['Time', 'UE-App', 'Length'])
    mw_time_start = -1

    times = []
    ue_apps = []
    lengths = []

    #for packet in capture.sniff_continuously():
    counter=0

    start_timer = time.time()
    for packet in capture:
        counter+=1
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

            times.append(packet.time)
            ue_apps.append(str(ue) + ": " + str(app))
            lengths.append(eval(packet.length))

            # for first time set time of first packet
            if mw_time_start == -1:
                mw_time_start = eval(packet.time)
        
            # check time
            mw_time_end = eval(packet.time)

            # check if mini window duration passed and we are ready to analyze mini window
            if mw_time_end - mw_time_start >= mini_window_duration and mw_time_start != -1:

                # if there are more than 1 mini-windows inside this time frame
                if mw_time_end - mw_time_start > 1.5:
                    elapsed_time = mw_time_end - mw_time_start
                    num_mw_inside = round(elapsed_time/mini_window_duration)

                    # we must break this to the appropriate mini-windows num



                    mw_num = len(mw_dict['UE1']['web-rtc'])



                    ######################### first packet to first mini-window
                    if mw_num == max_mws:
                        # drop first mini-window
                        mw_dict = drop_first(mw_dict)
                        
                        # count mini windows
                        mw_num = len(mw_dict['UE1']['web-rtc'])
                    
                    mw_dict = make_mini_window(mw_dict, times[0], ue_apps[0], lengths[0],one=1)
                    mw_num = len(mw_dict['UE1']['web-rtc'])


                    ## Data Collecting Mode: 
                    # Store Mini-Window to file
                    if mode == 0:
                        # store in csv format
                        store_mini_window(file_name,mw_dict)



                    # check if it is time to obtain X window
                    if mw_num == max_mws and mode == 1:
                        print("Obtain X window with {} mini-windows".format(mw_num))
                        
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


                    #################### for mini-windows in between, set them to zero
                    for i in range(1,num_mw_inside-1):

                        mw_num = len(mw_dict['UE1']['web-rtc'])
                        if mw_num == max_mws:
                            # drop first mini-window
                            mw_dict = drop_first(mw_dict)
                            
                            # count mini windows
                            mw_num = len(mw_dict['UE1']['web-rtc'])
                        
                        mw_dict = make_mini_window(mw_dict, [], [], [])


                        ## Data Collecting Mode: 
                        # Store Mini-Window to file
                        if mode == 0:
                            # store in csv format
                            store_mini_window(file_name,mw_dict)

                        # check if it is time to obtain X window
                        if mw_num == max_mws and mode == 1:
                            print("Obtain X window with {} mini-windows".format(mw_num))
                            
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



                    mw_num = len(mw_dict['UE1']['web-rtc'])

                    ############################# second packet to last mini-window
                    if mw_num == max_mws:
                        # drop first mini-window
                        mw_dict = drop_first(mw_dict)
                        
                        # count mini windows
                        mw_num = len(mw_dict['UE1']['web-rtc'])
                    
                    mw_dict = make_mini_window(mw_dict, times[1], ue_apps[1], lengths[1],one=1)


                    # re-init mini_window timer for next mini window
                    mw_time_start = -1

                    ## Data Collecting Mode: 
                    # Store Mini-Window to file
                    if mode == 0:
                        # store in csv format
                        store_mini_window(file_name,mw_dict)
                    
                    
                    # re-init mini-window df for next mini window
                    times = []
                    ue_apps = []
                    lengths = []

                    # check if it is time to obtain X window
                    if mw_num == max_mws and mode == 1:
                        print("Obtain X window with {} mini-windows".format(mw_num))
                        
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


                    continue



                print("Crop Mini Window:",mw_time_end - mw_time_start)
                # re-init mini_window timer for next mini window
                mw_time_start = -1

                # count mini windows
                mw_num = len(mw_dict['UE1']['web-rtc'])
                # ready to create mini-window data
                # if num of mini windows is already max_mws, we must drop the first mini-window
                if mw_num == max_mws:
                    # drop first mini-window
                    mw_dict = drop_first(mw_dict)
                    
                    # count mini windows
                    mw_num = len(mw_dict['UE1']['web-rtc'])

                # now create and append current mini-window
                mw_dict = make_mini_window(mw_dict, times, ue_apps, lengths)
                mw_num = len(mw_dict['UE1']['web-rtc'])



                ## Data Collecting Mode: 
                # Store Mini-Window to file
                if mode == 0:
                    # store in csv format
                    store_mini_window(file_name,mw_dict)
                
                
                # re-init mini-window df for next mini window
                times = []
                ue_apps = []
                lengths = []

                # check if it is time to obtain X window
                if mw_num == max_mws and mode == 1:
                    print("Obtain X window with {} mini-windows".format(mw_num))
                    
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


def make_mini_window(mw_dict, times, ue_apps, lengths,one=0):
    '''Finds the beggining indexes for each window'''
    
    if one==1:
        data = {'Time': [times], 'UE-App':[ue_apps], 'Length':[lengths]}
    else:
        data = {'Time': times, 'UE-App':ue_apps, 'Length':lengths}
    window = pd.DataFrame.from_dict(data)
    
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
            
            value = str(value[-1])
            if ue=='UE3' and app == 'web-server':
                # last packet
                f.write(value)
                f.write("\n")
            else:
                f.write(value)
                f.write(",")
        
    f.close()

if __name__ == "__main__":
    packet_parser(mini_window_duration=1, max_mws=2)
