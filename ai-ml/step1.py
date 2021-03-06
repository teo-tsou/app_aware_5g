import pandas as pd
import numpy as np
from numpy import array
import time
#from keras.models import load_model
import sys
import json
#import requests
from sqlalchemy import create_engine
import argparse
from pathlib import Path





def packet_parser(args,mini_window_duration=1, max_mws=30, mode=0, verbose=0, file_name="/dataset.csv"):
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

    # data structure to keep mws for predicitons
    X_mws = []

    # Data Collection mode: Init output file
   
    f = open(file_name,'w')
    f.write("UE1: web-rtc,UE1: sipp,UE1: web-server,UE2: web-rtc,UE2: sipp,UE2: web-server,UE3: web-rtc,UE3: sipp,UE3: web-server,Time\n")
    f.close()

    mw_num = 0
    mw_time_start = -1

    times = []
    ue_apps = []
    lengths = []

    db_connection_str = 'mysql://root:password@mysql.default/oai'
    db_connection = create_engine(db_connection_str)

    df = pd.read_sql('SELECT * FROM oai.app_data', con=db_connection)
    db_connection.dispose() 

    


    for i,packet in df.iterrows():

        if packet.Source == '192.168.3.101' or packet.Destination == '192.168.3.101' :
            app = 'web-rtc'
        if packet.Source == '192.168.3.102' or packet.Destination == '192.168.3.102' :
            app = 'sipp'
        if packet.Source == '192.168.3.103' or packet.Destination == '192.168.3.103' :
            app = 'web-server'
        if packet.Source == '192.168.20.2' or packet.Destination == '192.168.20.2' :
            ue = 'UE1'
        if packet.Source == '192.168.20.3' or packet.Destination == '192.168.20.3' :
            ue = 'UE2'
        if packet.Source == '192.168.20.4' or packet.Destination == '192.168.20.4' :
            ue = 'UE3'

        times.append(packet.Time_packet)
        ue_apps.append(str(ue) + ": " + str(app))
        lengths.append(eval(packet.Length_packet))

        # for first time set time of first packet
        if mw_time_start == -1:
            mw_time_start = eval(packet.Time_packet)

        # check time
        mw_time_end = eval(packet.Time_packet)

        # check if mini window duration passed and we are ready to analyze mini window
        if mw_time_end - mw_time_start >= mini_window_duration and mw_time_start != -1:

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
                    
                    mw_dict = make_mini_window(mw_dict, new_times, new_ue_apps,new_lengths)
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
                        #X_list = array_x(mw_dict)
                        
                        # scale 
                        #X_scaled = scale_x(X_list,max_mws)
                        
                        # predict
                        #yhat = predict(X_list,max_mws)

                        # post slice
                        #post_slice(yhat)

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
                    #X_list = array_x(mw_dict)
                    
                    # scale 
                    #X_scaled = scale_x(X_list,max_mws)
                    
                    # predict
                    #yhat = predict(X_list,max_mws)

                    # post slice
                    #post_slice(yhat)

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
            mw_dict = make_mini_window(mw_dict, times, ue_apps, lengths)
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
                #X_list = array_x(mw_dict)
                
                # scale 
                #X_scaled = scale_x(X_list,max_mws)
                #print(X_list)
                # predict
                #yhat = predict(X_list,max_mws)

                # post slice
                #post_slice(yhat)

            elif mw_num > max_mws:
                print("[ERROR]: Mini-windows surpassed max limit!")
                exit()

    df = pd.read_csv(file_name)
    dict = df.to_dict('list')
    with open(args.data, 'w') as out_file:
        json.dump(dict, out_file)

    return           


def make_mini_window(mw_dict, times, ue_apps, lengths,one=0):
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
    # crop window    
    length_sum = dict(window.groupby('UE-App')['Length'].sum())
    window_combs = list(window['UE-App'].unique())
    #print(length_sum)
    for key, value in mw_dict.items():
        if key == 'Time':
            if time0 == []:
                mw_dict[key].append('-')
            else:
                mw_dict[key].append(time0)
            continue
        for j in list(mw_dict[key].keys()):
            comb = str(key) + ": " + str(j)
            
            if comb in window_combs:
                stored_value = length_sum[comb]
                if stored_value > 0 :
                    stored_value = 1
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
        for app in list(mw_dict[ue].keys()):
            # for every app 

            temp_list = mw_dict[ue][app]
            del temp_list[0]

            mw_dict[ue][app] = temp_list

    return mw_dict



def keep_mws_as_df(mw_dict,verbose=2):
    mw = []

    for ue, stats in mw_dict.items():
        # for every ue
        if ue == 'Time':
            continue

        for app, value in stats.items():
            # for ever app
            
            value = value[-1]
            mw.append(value)

    return np.array(mw)


def store_mini_window(file_name, mw_dict):
    f = open(file_name,'a')

    for ue, stats in mw_dict.items():
        # for every ue
        if ue == 'Time':
            f.write(mw_dict['Time'][-1])
            f.write("\n")
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

if __name__ == "__main__":
    
    # This component does not receive any input
    # it only outpus one artifact which is `data`.
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str)
    
    args = parser.parse_args()
    
    # Creating the directory where the output file will be created 
    # (the directory may or may not exist).
    Path(args.data).parent.mkdir(parents=True, exist_ok=True)

    packet_parser(args,mini_window_duration=1, max_mws=5, mode=0)

    






