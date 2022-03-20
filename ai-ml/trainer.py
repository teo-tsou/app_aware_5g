import os
import pandas as pd
import numpy as np
from tensorflow.keras import Sequential
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import GRU
from tensorflow.keras.layers import Dense
from os import walk
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error

from random import random
from random import randint
from numpy import array
from numpy import zeros
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import TimeDistributed

from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import TimeDistributed
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import RepeatVector
from tensorflow.keras.layers import Bidirectional
from tensorflow.keras.layers import GRU

from numpy import array
from numpy import hstack
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from sklearn.preprocessing import MinMaxScaler




def extract_X_y_from_file(array, X_num, y_num):
    """ 
    Function that pre-process the data with a sliding-window supervised 
    learning approach extracting X and y

    - X_num: Input Window Length (N)
    - y_num: Number of prediction time-steps (M). We calculate the y as a mean 
              of the next M time-slots.
    """

    X = []
    y = []
    
    iterations = len(array)
    for i in range(iterations):
        ### check if we reach to end
        if i+X_num + y_num > len(array):
            break
            
        ### calculate X,y
        X_temp = array[i: i+X_num]
        y_temp = array[i+X_num: i+X_num + y_num]
        
        ### format y use mean
        new_y_temp = []
        # for every column
        for j in range(15):
            j_temp = []
            # for every row
            for i in range(y_num):
                row = y_temp[i][j]                

                j_temp.append(row)

            # obtain mean
            new_y_temp.append(np.mean(j_temp))
                        
        
        # append
        X.append(X_temp)
        y.append(new_y_temp)        
        
    return X,y


def create_data(df, X_num = 30, y_num = 5):
    """
    Function that reads all data csvs and calls the above mentioned function to
    extract X and y
    """
    all_X = []
    all_y = []

    # convert to list
    array = df.values.tolist()

    # create X and y
    X,y = extract_X_y_from_file(array, X_num, y_num)

    # add to final data
    all_X = all_X + X
    all_y = all_y + y

    return all_X, all_y


if __name__ == "__main__":
    train_df = pd.read_csv('train_data2_range0_15.csv')
    test_df = pd.read_csv('data_range_0_15.csv')
    test_df = test_df.drop(['Time'],axis=1)
    test_df = test_df.drop(['empty'],axis=1)


    train_df['UE1-Jitter'] = train_df['UE1-Jitter'].astype(float)
    train_df['UE2-Jitter'] = train_df['UE2-Jitter'].astype(float)
    train_df['UE3-Jitter'] = train_df['UE3-Jitter'].astype(float)


    test_df['UE1-Jitter'] = test_df['UE1-Jitter'].astype(float)
    test_df['UE2-Jitter'] = test_df['UE2-Jitter'].astype(float)
    test_df['UE3-Jitter'] = test_df['UE3-Jitter'].astype(float)

    ### Normalizing Data

    # Create a scaler object
    scaler = MinMaxScaler()
    # Fit and transform the data
    train_df_normalized = pd.DataFrame(scaler.fit_transform(train_df), columns=train_df.columns)
    test_df_normalized = pd.DataFrame(scaler.transform(test_df), columns=test_df.columns)

    ### Sliding-Window Approach
    
    #Create windows of data with the sliding-window technique to construct a supervised learning problem.
    
    all_X, all_y = create_data(df=train_df_normalized)
    X_data = np.array(all_X)
    y_data = np.array(all_y)

    #Pre-process the basic non-augmented scenario to use as validation data.

    val_X = []
    val_y = []
    val_X, val_y = create_data(df=test_df_normalized)
    X_val = np.array(val_X)
    y_val = np.array(val_y)
    

    ###CNN-LSTM Model Implementation

    # define the model
    model = Sequential()
    model.add(Conv1D(filters=64, kernel_size=2, activation='relu', input_shape=(30,15)))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Flatten())
    model.add(RepeatVector(1))
    model.add(LSTM(25, activation='relu', return_sequences=True))
    model.add(LSTM(25, activation='relu'))
    model.add(Dense(15))
    model.compile(optimizer='adam', loss='mse')
    model.fit(X_data,y_data, validation_data=(X_val,y_val),epochs=100, callbacks=callbacks_list)
