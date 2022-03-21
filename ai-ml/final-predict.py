import pyshark
import ipaddress
import pandas as pd
import numpy as np
from numpy import array
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import LSTM
#from tensorflow.keras.layers import Dense
from sklearn.preprocessing import MinMaxScaler
#import matplotlib.pyplot as plt
import time
import math
import tensorflow
from tensorflow.keras.models import load_model
import sys
import json
import requests
from statistics import mean
import joblib

# load scaler
scaler = joblib.load("/mnt/v2_train_scaler_app_aware_CNN-LSTM.save")

# load model
model = load_model('/mnt/v2__app_aware_CNN-LSTM_15cols__train_data2_range0_15__test_datarange0-15.best.hdf5')

def packet_parser(mini_window_duration=1, max_mws=30, mode=0, verbose=0, debug=0, file_name= "/mnt/check.csv"):
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
    mw_dict['Time'] = []
    mw_dict['UE1-Jitter'] = []
    mw_dict['UE2-Jitter'] = []
    mw_dict['UE3-Jitter'] = []
    mw_dict['UE1-CQI'] = []
    mw_dict['UE2-CQI'] = []
    mw_dict['UE3-CQI'] = []



    # data structure to keep mws for predicitons
    X_mws = []

    # Data Collection mode: Init output file
   
    f = open(file_name,'w')
    f.write("UE1: web-rtc,UE1: sipp,UE1: web-server,UE2: web-rtc,UE2: sipp,UE2: web-server,UE3: web-rtc,UE3: sipp,UE3: web-server,Time,UE1-Jitter,UE2-Jitter,UE3-Jitter,UE1-CQI,UE2-CQI,UE3-CQI\n")
    f.close()
    mw_num = 0
    if debug==0:
        capture = pyshark.LiveCapture(interface='net3',only_summaries= True, display_filter = "(tcp or udp or sip or stun or dtls ) and ((ip.src==192.168.3.0/24 and ip.dst==192.168.20.0/24) or (ip.src==192.168.20.0/24 and ip.dst==192.168.3.0/24))")
        #capture = pyshark.FileCapture('traffic.pcap',only_summaries= True, display_filter = "(tcp or udp or sip or stun or dtls ) and ((ip.src==192.168.3.0/24 and ip.dst==192.168.20.0/24) or (ip.src==192.168.20.0/24 and ip.dst==192.168.3.0/24))")
    else:
        #capture = pyshark.FileCapture('traffic.pcap',only_summaries= True, display_filter = "(tcp or udp or sip or stun or dtls ) and ((ip.src==192.168.3.0/24 and ip.dst==192.168.20.0/24) or (ip.src==192.168.20.0/24 and ip.dst==192.168.3.0/24))")
        capture = pyshark.LiveCapture(interface='net3',only_summaries= True, display_filter = "(tcp or udp or sip or stun or dtls ) and ((ip.src==192.168.3.0/24 and ip.dst==192.168.20.0/24) or (ip.src==192.168.20.0/24 and ip.dst==192.168.3.0/24))")
    #mini_window_df = pd.DataFrame(columns = ['Time', 'UE-App', 'Length'])
    mw_time_start = -1

    times = []
    ue_apps = []
    lengths = []
    ue1_time = []
    ue2_time = []
    ue3_time = []
    ue1_jitter = []
    ue2_jitter = []
    ue3_jitter = []
    names = []
    ue1_jitter_mw_avg = 0
    ue2_jitter_mw_avg = 0
    ue3_jitter_mw_avg = 0
    cqi = []
    ue1_cqi = 0
    ue2_cqi = 0
    ue3_cqi = 0
    ue1_length = []
    ue2_length = []
    ue3_length = []

    for packet in capture.sniff_continuously():
    #for packet in capture:

        counter=1

        #start_timer = time.time()
        #for packet in capture:
            # counter+=1

            # # check that you dont miss packets
            # if packet.no != '2' and packet.no != str(counter):
            #     print('problem: Counter=',counter,'packet no=',packet.no)
            #     exit()

        times.append(packet.time)   
                
            # append to mini-window df every filtered packet
        if packet.source == '192.168.3.101' or packet.destination == '192.168.3.101' :
            app = 'web-rtc'
        if packet.source == '192.168.3.102' or packet.destination == '192.168.3.102' :
            app = 'sipp'
        if packet.source == '192.168.3.103' or packet.destination == '192.168.3.103' :
            app = 'web-server'
        if packet.source == '192.168.20.2' or packet.destination == '192.168.20.2' :
            ue = 'UE1'
            ue1_time.append(packet.time)
            ue1_length.append(eval(packet.length))
        if packet.source == '192.168.20.3' or packet.destination == '192.168.20.3' :
            ue = 'UE2'
            ue2_time.append(packet.time)
            ue2_length.append(eval(packet.length))
        if packet.source == '192.168.20.4' or packet.destination == '192.168.20.4' :
            ue = 'UE3'
            ue3_time.append(packet.time)
            ue3_length.append(eval(packet.length))


        
        ue_apps.append(str(ue) + ": " + str(app))
        lengths.append(eval(packet.length))
        
        

        # for first time set time of first packet
        if mw_time_start == -1:
            mw_time_start = eval(packet.time)

        # check time
        mw_time_end = eval(packet.time)

        # check if mini window duration passed and we are ready to analyze mini window
        if mw_time_end - mw_time_start >= mini_window_duration and mw_time_start != -1:
            
            #Calculate Jitter in mini window duration for each UE:
            
               #UE1:
            if sum(ue1_length) != 0:
                for t in range(len(ue1_time) -1):
                    jitter_ue1 = eval(ue1_time[t+1]) - eval(ue1_time[t])
                    ue1_jitter.append(jitter_ue1)
                    ue1_jitter_mw_avg = mean(ue1_jitter)
                    #print(f'MEAN JITTER APO UE1: {ue1_jitter_mw_avg}')
                jitter_ue1 = []
                ue1_time = []
                ue1_length = []

            else: 
                ue1_jitter_mw_avg = 0
                jitter_ue1 = []
                ue1_time = []
                ue1_length = []
            
                #UE2:
            if sum(ue2_length) != 0:
                for t in range(len(ue2_time) -1):
                    jitter_ue2 = eval(ue2_time[t+1]) - eval(ue2_time[t])
                    ue2_jitter.append(jitter_ue2)
                    ue2_jitter_mw_avg = mean(ue2_jitter)
                    #print(f'MEAN JITTER APO UE2: {ue2_jitter_mw_avg}')
                jitter_ue2 = []
                ue2_time = []
                ue2_length = []
            else: 
                ue2_jitter_mw_avg = 0
                jitter_ue2 = []
                ue2_time = []
                ue2_length = []


                #UE3:
            if sum(ue3_length) != 0:
                for t in range(len(ue3_time) -1):
                    jitter_ue3 = eval(ue3_time[t+1]) - eval(ue3_time[t])
                    ue3_jitter.append(jitter_ue3)
                    ue3_jitter_mw_avg = mean(ue3_jitter)
                jitter_ue3 = []
                ue3_time = []
                ue3_length = []
            else: 
                ue3_jitter_mw_avg = 0
                jitter_ue3 = []
                ue3_time = []
                ue3_length = []
            
            
            # Monitoring - Collecting CQI

            URL = "http://192.168.18.202:9999/stats/"

            r = requests.get(url = URL)

            # extracting data in json format 
            data = r.json()

            # Find every instance of `wbCqi` in a Python dictionar$
            names = json_extract(data, 'wbCqi')

            ue1_cqi = names[0]
            ue2_cqi = names[1]
            ue3_cqi = names[2]

            names = []


            
                
            # if there are more than 1 mini-windows inside this time frame
            if mw_time_end - mw_time_start > 1.5:
                # we must break this to the appropriate mini-windows num
                # we will find the num of mini-windows that exist inside the time frame elapsed time of the two packets
                # then we will assign the first packet to the first mini-window and the second packet to the last mini-window
                # we will fill the mini-windows in between with zeroes

                # elapsed time
                elapsed_time = mw_time_end - mw_time_start 

                # num of mini-windows that we need to create
                num_mw_inside = round(elapsed_time/mini_window_duration)

                # new duration of new mini-windows
                new_duration = (float)(elapsed_time/num_mw_inside)

                #print("MANY MINI-WINDOWS: ",elapsed_time,'mw_time_start',mw_time_start,'num_mw_inside',num_mw_inside,'TIMES',times)
                
                #################### for mini-windows in between
                for i in range(num_mw_inside):

                    # find indexes
                    new_times = []
                    new_lengths = []
                    new_ue_apps = []
                    for c_time, c_ue_app, c_length in zip(times, ue_apps, lengths):

                        # obtain times that are for every new mini-window
                        if eval(c_time) >= mw_time_start + i*new_duration and eval(c_time) <= mw_time_start + (i+1)*new_duration:
                            new_times.append(c_time+'-')
                            new_lengths.append(c_length)
                            new_ue_apps.append(c_ue_app)

                    #print("Found : ",new_times,new_lengths)
                    
                    mw_num = len(mw_dict['UE1']['web-rtc'])
                    if mw_num == max_mws:
                        # drop first mini-window
                        mw_dict = drop_first(mw_dict)
                        
                        # count mini windows
                        mw_num = len(mw_dict['UE1']['web-rtc'])
                    
                    mw_dict = make_mini_window(mw_dict, new_times, new_ue_apps,new_lengths, ue1_jitter_mw_avg, ue2_jitter_mw_avg ,ue3_jitter_mw_avg, ue1_cqi, ue2_cqi, ue3_cqi)
                    # count mini windows
                    mw_num = len(mw_dict['UE1']['web-rtc'])

                    ## Data Collecting Mode: 
                    # Store Mini-Window to file
                    if mode == 0:
                        # store in csv format
                        store_mini_window(file_name,mw_dict)

                    # check if it is time to obtain X window
                    if mw_num == max_mws and mode == 1:
                        if verbose:
                            print("Obtain X window with {} mini-windows".format(mw_num))
                        
                        # obtain X window, from all mini_windows
                        # to array

                       

                        X_list = array_x(mw_dict)

                    

                        # scale 
                        X_scaled = scale_x(X_list)
                        
                        # predict
                        yhat = predict(X_scaled)

                        #post slice
                        post_slice(yhat, debug=debug)

                    elif mw_num > max_mws:
                        print("[ERROR]: Mini-windows surpassed max limit!")
                        exit()    

                
                # re-init mini_window timer for next mini window
                mw_time_start = -1
                
                # re-init mini-window df for next mini window
                times = []
                ue_apps = []
                lengths = []

                # check if it is time to obtain X window
                if mw_num == max_mws and mode == 1:
                    if verbose:
                        print("Obtain X window with {} mini-windows".format(mw_num))
                    
                    # obtain X window, from all mini_windows
                    # to array

                    X_list = array_x(mw_dict)
                    

                    # scale 
                    X_scaled = scale_x(X_list)
                    
                    # predict
                    yhat = predict(X_scaled)

                    # post slice
                    post_slice(yhat, debug=debug)

                elif mw_num > max_mws:
                    print("[ERROR]: Mini-windows surpassed max limit!")
                    exit()    


                continue

            ######################################

            #time.sleep(1)

            if verbose:
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
            mw_dict = make_mini_window(mw_dict, times, ue_apps, lengths, ue1_jitter_mw_avg ,ue2_jitter_mw_avg ,ue3_jitter_mw_avg, ue1_cqi, ue2_cqi, ue3_cqi)
            mw_num = len(mw_dict['UE1']['web-rtc'])



            ## Data Collecting Mode: 
            # Store Mini-Window to file
            if mode == 0:
                # store in csv format
                store_mini_window(file_name,mw_dict)

            else:
                # keep mw as df
                keep_mws_as_df(mw_dict)
                store_mini_window(file_name,mw_dict)
                
            
            
            # re-init mini-window df for next mini window
            times = []
            ue_apps = []
            lengths = []

            # check if it is time to obtain X window
            if mw_num == max_mws and mode == 1:
                if verbose:
                    print("Obtain X window with {} mini-windows".format(mw_num))
                
                # obtain X window, from all mini_windows
                # to array
                # Always there!
                X_list = array_x(mw_dict)
                X_scaled = scale_x(X_list)
                #print(X_list)
                # predict
                yhat = predict(X_scaled)

                # post slice
                post_slice(yhat,debug=debug)

            elif mw_num > max_mws:
                print("[ERROR]: Mini-windows surpassed max limit!")
                exit()    
    return           


def make_mini_window(mw_dict, times, ue_apps, lengths, jitter1, jitter2, jitter3, cqi1, cqi2, cqi3, one=0):
    '''Finds the beggining indexes for each window'''
    
    if one==1:
        data = {'Time': [times], 'UE-App':[ue_apps], 'Length':[lengths]}
        if times == []:
            time0 = '-'
        else:
            time0 = times
    else:
        data = {'Time': times, 'UE-App':ue_apps, 'Length':lengths}
        if times == []:
            time0 = '-'
        else:
            time0 = times[0]
    window = pd.DataFrame.from_dict(data)
    #print(data)
    #crop window    
    length_sum = dict(window.groupby('UE-App')['Length'].sum())
    window_combs = list(window['UE-App'].unique())
    #print(length_sum)
    
    for key, value in mw_dict.items():

        if key == 'UE1-Jitter':
            mw_dict[key].append(jitter1)
        if key == 'UE2-Jitter':
            mw_dict[key].append(jitter2)
        if key == 'UE3-Jitter':
            mw_dict[key].append(jitter3)

        if key == 'UE1-CQI':
             mw_dict[key].append(cqi1)
        if key == 'UE2-CQI':
            mw_dict[key].append(cqi2)
        if key == 'UE3-CQI':   
            mw_dict[key].append(cqi3)    

        if key == 'Time':
            if time0 == []:
                mw_dict[key].append('-')
            else:
                mw_dict[key].append(time0)
            continue



        if key == 'UE1-Jitter' or key == 'UE2-Jitter' or key == 'UE3-Jitter':
            continue

        if key == 'UE1-CQI' or key == 'UE2-CQI' or key == 'UE3-CQI':
            continue  
        
        for j in list(mw_dict[key].keys()):
            comb = str(key) + ": " + str(j)
            
            if comb in window_combs:
                stored_value = length_sum[comb]
                if stored_value > 0 :
                    stored_value = length_sum[comb]
                else:
                    stored_value = 0


                mw_dict[key][str(j)].append(stored_value)
            else:
                mw_dict[key][str(j)].append(0) 
    return mw_dict

def drop_first(mw_dict):
    for ue,stats in mw_dict.items():
        # for every ue
        if ue == 'Time':
            continue

        if ue == 'UE1-Jitter' or ue == 'UE2-Jitter' or ue == 'UE3-Jitter':
            temp_list = mw_dict[ue]
            del temp_list[0]
            mw_dict[ue] = temp_list
            continue

        if ue == 'UE1-CQI' or ue == 'UE2-CQI' or ue == 'UE3-CQI':
            temp_list = mw_dict[ue]
            del temp_list[0]
            mw_dict[ue] = temp_list
            continue 
       
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

    #print('iters',iters)
    #print('X',X)

    for i in range(iters):
        counter = 0
        temp_list = []
        for ue, stats in X.items():
            #print(stats)
            # for every ue
            if ue == 'Time':
                continue

            if ue == 'UE1-Jitter' or ue == 'UE2-Jitter' or ue == 'UE3-Jitter':
                temp_list.append(stats[i])
                continue

            if ue == 'UE1-CQI' or ue == 'UE2-CQI' or ue == 'UE3-CQI':
                temp_list.append(stats[i])
                continue 

            # for every column
            for app, values in stats.items():
                # for ever app 
                #print('values',values)
                temp_list.append(values[i])
            counter+=1

        X_list.append(temp_list)

    #print('X_list',X_list)

    return np.array(X_list)   


def scale_x(X_list,verbose=2, max_mw=30):
    
    input_df = pd.DataFrame(X_list, columns = ["UE1: web-rtc","UE1: sipp","UE1: web-server","UE2: web-rtc","UE2: sipp","UE2: web-server","UE3: web-rtc","UE3: sipp","UE3: web-server","UE1-Jitter","UE2-Jitter","UE3-Jitter","UE1-CQI","UE2-CQI","UE3-CQI"])
    #print(input_df)
    input_df['UE1-Jitter'] = input_df['UE1-Jitter'].astype(float)
    input_df['UE2-Jitter'] = input_df['UE2-Jitter'].astype(float)
    input_df['UE3-Jitter'] = input_df['UE3-Jitter'].astype(float)

    #print(input_df.dtypes)
    scaled_df = scaler.transform(input_df)
    #print(scaled_df)
    # input_df_normalized = pd.DataFrame(scaler.fit_transform(input_df), columns=input_df.columns)
    # exit()
    # To Do:  here we will load the scaler used in model training 
    # flattened = np.array(X_list).reshape(-1,1)
    # rescaled = scaler.fit_transform(flattened)
    
    X_scaled = scaled_df.reshape(1,max_mw,15)

    return X_scaled

def predict(X_scaled,verbose=2):
    print(X_scaled)
    print(X_scaled.shape)
    yhat = model.predict(X_scaled)

    if verbose == 2:
        print('\n\n')
        print('           ______________________________         ')
        print('|#########|                              |#########|')
        print('|~~~~~~~~~|   Service-aware AI/ML Unit   |~~~~~~~~~|')
        print('|#########|______________________________|#########|')
        print()
        print("|#####~~~~~~~~~~~  Input Window  ~~~~~~~~~~~~~#####|")
        print(str(X_scaled))
        #print("yhat:"+str(yhat)+"\n\n")

    return yhat

def filter_thresholds(web_rtc, sipp, web_server, jitter, cqi):
    # thresholds: 
    # 1) app: 
    #           0 (web_server), 
    #           1 (sipp), 
    #           2 (web_rtc)
    #
    # 2) length (l): 
    #           0 (l < 25000), 
    #           1     (25000 < l < 50000), 
    #           2                 (50000 < l)
    #
    # 3) jitter (j): 
    #           0 (j < 5), 
    #           1     (5 < j < 10), 
    #           2             (10 < j)
    #
    # 4) cqi (c): 
    #           0             (11 < c), 
    #           1     (9 < c < 11), 
    #           2 (c < 9)

    # 1) app
    if web_rtc > 0:
        app = 2
    elif sipp > 0:
        app = 1
    else:
        app = 0

    # 2) length
    total_sum = web_rtc + sipp + web_server
    if total_sum > 50000:
        length = 2
    elif total_sum <= 50000 and total_sum > 25000:
        length = 1
    else:
        length = 0

    # 3) jitter
    ms_jitter = jitter*1000 # convert to ms from secs
    if ms_jitter > 10:
        jitter = 2
    elif ms_jitter <= 10 and ms_jitter > 5:
        jitter = 1
    else:
        jitter = 0

    # 4) cqi
    if cqi <= 9:
        cqi = 2
    elif cqi <= 11 and cqi > 9:
        cqi = 1
    else:
        cqi = 0

    return app, length, jitter, cqi

def post_slice(yhat,verbose=2,debug=0):
    # Implement an efficient scheduling policy:
    #
    # Criteria:
    # a) App,  b) Throughput,  c) Jitter,  d) CQI 
    
    # inverse scaling to the original scale 
    yhat_inverse = scaler.inverse_transform(yhat)
    yhat_inverse = yhat_inverse[0]
    f = open('yhat_inverse.txt','a')
    f.write(str(yhat_inverse))
    f.write("\n")
    


    # print logs
    if verbose == 2:
        print()
        print("|#####~~~~~~~~~~~~  Predictions  ~~~~~~~~~~~~~#####|")
        print('| - model\'s yhat (next 5sec): \n ',yhat)
        print('|')
        print('| - original scale yhat (next 5sec): \n ',yhat_inverse)
        print('|')


    # define coeffs, the weights for every criteria of the mathematical formula
    coeff_a = 4     # app
    coeff_b = 4     # throughput
    coeff_c = 4     # jitter
    coeff_d = 4     # cqi

    # Obtain predicted values for every UE
    n_ues = 3
    slices = []
    
    for ue in range(n_ues):
        # parse UE's throughputs
        web_rtc = yhat_inverse[ue + 0]
        sipp = yhat_inverse[ue + 1]
        web_server = yhat_inverse[ue + 2]

        # parse UE's jitter
        jitter = yhat_inverse[ue+9]

        # parse UE's CQI
        cqi = yhat_inverse[ue+12]

        # filter with thresholds and define the level of priority for every criteria
        app, length, jitter, cqi = filter_thresholds(web_rtc, sipp, web_server, jitter, cqi)

        # make a decision for the slice's percentage value, based on the mathematical formula
        decision = coeff_a * app + coeff_b * length + coeff_c * jitter + coeff_d * cqi

        # append
        slices.append(decision)

    # In this point, all the new slice's percentages are ready
    # Check if this slice is different from the existing slice
    post_configure(slices[0], slices[1], slices[2], debug=0)

    if verbose == 2:
        print('|')
        print('|#####~~~~~~~~~~~~  Slicing Policy  ~~~~~~~~~~~~~#####|')

    # comparison
    #if slices != curr_slices:
        # post new slice
    

        # print ue's slice
        for ue in range(n_ues):
            print('| - UE ',ue+1,': ',slices[ue],'%')
        print('|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|')
    else:
        # no need to post the slice
        # print ue's slice
        for ue in range(n_ues):
            print('| - UE ',ue+1,': ',slices[ue],'%')
        print('|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|')















    # make a policy based on yhat
    # need_post = 0


    # ue_app_pairs = ['UE1: web-rtc','UE1: sipp','UE1: web-server','UE2: web-rtc','UE2: sipp',
    #             'UE2: web-server','UE3: web-rtc','UE3: sipp','UE3: web-server']

    # predicted = []

    # new_y_hat = np.array([round(i) for i in yhat[0]])
    # if verbose == 2:
    #     print()
    #     print("|#####~~~~~~~~~~~~  Predictions  ~~~~~~~~~~~~~#####|")
    #     print('Rounded yhat (next 5sec): \n ',new_y_hat)
    #     print()
    #     print('------------------------------------------')
    #     print('|      yhat Translation (next 5sec):      ')
    #     print("|      -----------------------------      ")

    # for i in range(len(new_y_hat)):
    #     if new_y_hat[i] == 1:
    #         if verbose == 2:
    #             print('|      ',ue_app_pairs[i])
    #         predicted.append(ue_app_pairs[i])
    # if verbose == 2:
    #     print('----------------------------------')


    # # GET slices percentage
    # if debug == 0:
    #     curr_slices = get_slices()
    # else:
    #     curr_slices = [8,8,8]
    


    # ### decide slicing policy
    # # We want to investigate the predictions
    # # If we find Web-rtc app(s), we must raise the 
    # # percentage(s) of the corresponding UEs


    # ### Web-RTC ###
    # # UE1
    # if 'UE1: web-rtc' in predicted and curr_slices[0]==8:
    #     need_post = 1
    #     slice0 = 40
    # elif 'UE1: web-rtc' not in predicted and curr_slices[0]==40:
    #     need_post = 1
    #     slice0 = 8
    # else:
    #     slice0 = curr_slices[0]

    # # UE2
    # if 'UE2: web-rtc' in predicted and curr_slices[1]==8:
    #     need_post = 1
    #     slice1 = 40
    # elif 'UE2: web-rtc' not in predicted and curr_slices[1]==40:
    #     need_post = 1
    #     slice1 = 8
    # else:
    #     slice1 = curr_slices[1]    

    # # UE3
    # if 'UE3: web-rtc' in predicted and curr_slices[2]==8:
    #     need_post = 1
    #     slice2 = 40
    # elif 'UE3: web-rtc' not in predicted and curr_slices[2]==40:
    #     need_post = 1
    #     slice2 = 8
    # else:
    #     slice2 = curr_slices[2]    

    # if need_post == 1:
    #     post_configure(slice0, slice1, slice2, debug=debug)
    #     need_post = 0    

    # if verbose == 2:
    #     print()
    #     print('----------------------------------')
    #     print('|      Slicing Policy:      ')
    #     print("|      ---------------      ")
    #     if slice0 == 40:
    #         print('|      UE1 -> More Resources')
    #     else:
    #         print('|      UE1 -> Normal Resources')

    #     if slice1 == 40:
    #         print('|      UE2 -> More Resources')
    #     else:
    #         print('|      UE2 -> Normal Resources')

    #     if slice2 == 40:
    #         print('|      UE3 -> More Resources')
    #     else:
    #         print('|      UE3 -> Normal Resources')
    #     print('----------------------------------')




def keep_mws_as_df(mw_dict,verbose=2):
    mw = []

    for ue, stats in mw_dict.items():
        # for every ue
        if ue == 'Time':
            continue

        

        if ue == 'UE1-Jitter' or ue == 'UE2-Jitter' or ue == 'UE3-Jitter':
            mw.append(stats[-1])
            continue

        if ue == 'UE1-CQI' or ue == 'UE2-CQI' or ue == 'UE3-CQI':
            mw.append(stats[-1])
            continue 

        for app, value in stats.items():
            # for ever app
            
            value = value[-1]
            mw.append(value)
    # if verbose == 2:
    #     print("\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #     print("NEW Mini-window: "+str(np.array(mw)))
    #     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


    return np.array(mw)


def store_mini_window(file_name, mw_dict):
    f = open(file_name,'a')

    for ue, stats in mw_dict.items():
        # for every ue

        if ue == 'UE1-Jitter':
            f.write(str(mw_dict[ue][-1]))
            f.write(",")
        if ue == 'UE2-Jitter':
            f.write(str(mw_dict[ue][-1]))
            f.write(",")
        if ue == 'UE3-Jitter':   
           f.write(str(mw_dict[ue][-1]))
           f.write(",")
        
        if ue == 'UE1-Jitter' or ue == 'UE2-Jitter' or ue == 'UE3-Jitter':
            continue    


        if ue == 'UE1-CQI':
            f.write(str(mw_dict[ue][-1]))
            f.write(",")
        if ue == 'UE2-CQI':
            f.write(str(mw_dict[ue][-1]))
            f.write(",")
        if ue == 'UE3-CQI':   
           f.write(str(mw_dict[ue][-1]))
           f.write(",")  
           f.write("\n") 

        if ue == 'UE1-CQI' or ue == 'UE2-CQI' or ue == 'UE3-CQI':
            continue    


        if ue == 'Time':
            f.write(mw_dict['Time'][-1])
            #f.write("\n")
            f.write(",")
            continue
        
         

        for app, value in stats.items():
            # for ever app
            
            value = str(value[-1])
            if ue=='UE3' and app == 'web-server':
                # last packet
                f.write(value)
                f.write(",")
            else:
                f.write(value)
                f.write(",")
        
    f.close()


def rnti_parser(ues = 3):
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
                        # if ue['imsi'] != '0':
                            #if ue['rnti'] not in rnti:
                        rnti.append(ue['rnti'])
                    if len(rnti) < ues:
                        rnti = []
                    else:
                        all_ues = 1
                else:
                    break
    return(rnti)             


def get_slices():

    URL = "http://192.168.18.202:9999/stats/"

    ### ~~~ GET ~~~ ###
    # sending get request and saving the response as respo$
    r = requests.get(url = URL)
    
    # extracting data in json format 
    data = r.json()

    # Find every instance of `wbCqi` in a Python dictionar$
    slices = json_extract(data, 'percentage')

    return slices 

def json_extract(obj, key):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values

def post_configure(slice0, slice1, slice2, debug=0):
    # defining the api-endpoint
    f = open('slices.txt','a')
    f.write(str(slice0))
    f.write(",")
    f.write(str(slice1))
    f.write(",")
    f.write(str(slice2))
    f.write("\n")
    

    API_ENDPOINT = "http://192.168.18.202:9999/slice/enb/-1"

    data = {
        "ul": [
            {
                "id": 0,
                "percentage":16,
                "maxmcs": 16
            },
            {
                "id": 1,
                "percentage":17,
                "maxmcs": 16
            },
            {
                "id": 2,
                "percentage":16,
                "maxmcs": 16
            }
        ],
        "dl": [
            {
                "id": 0,
                "percentage":slice0,
                "maxmcs": 26
            },
            {
                "id": 1,
                "percentage":slice1,
                "maxmcs": 26
            },
            {
                "id": 2,
                "percentage":slice2,
                "maxmcs": 26
            }
        ],
        "intrasliceShareActive": True,
        "intersliceShareActive": True
    }

    # sending post request and saving response as response object 
    if debug ==0:
        r = requests.post(url = API_ENDPOINT, json = data) 


def post_assoc(rnti):

    API_ENDPOINT = "http://192.168.18.202:9999/ue_slice_assoc/enb/-1"
    
    if len(rnti) == 3:
        assoc1 = {
            "ueConfig": [
                {
                    "rnti": rnti[0],
                    "dlSliceId": 0
                }
            ]
        }
        r = requests.post(url = API_ENDPOINT, json = assoc1)
        time.sleep(2)
        assoc2 = {
            "ueConfig": [
                {
                    "rnti": rnti[1],
                    "dlSliceId": 1
                }
            ]
        }
        r = requests.post(url = API_ENDPOINT, json = assoc2)
        time.sleep(2)
        assoc3 = {
            "ueConfig": [
                {
                    "rnti": rnti[2],
                    "dlSliceId": 2
                }
            ]
        }

        r = requests.post(url = API_ENDPOINT, json = assoc3) 


def init_slice(ues=3,slice0=8,slice1=8,slice2=8):
    rnti = rnti_parser(ues)
    time.sleep(3.5)
    post_configure(slice0,slice1,slice2)
    time.sleep(0.5)
    post_assoc(rnti)   

if __name__ == "__main__":
    init_slice(ues = 3, slice0=8, slice1=8, slice2=8)
    packet_parser(mini_window_duration=1, max_mws=30, mode=1,verbose=0, debug=1)


