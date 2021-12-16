import pandas as pd
import argparse
from pathlib import Path
import json
import numpy as np
from tensorflow.keras import Sequential
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dense


def step3(args):
    
    X = json.loads(args.data_x)
    y = json.loads(args.data_y)


    model = Sequential()
    model.add(LSTM(25, activation='relu',  return_sequences=True, input_shape=(5, 9)))
    model.add(LSTM(25, activation='relu'))
    model.add(Dense(9))
    model.compile(optimizer='adam', loss='mse')
    print(model.summary()) 
    model.fit(X,y,epochs=5)
    model.save('/mnt/')
    model_save_name = 'lstm.h5'
    path = f"/mnt/{model_save_name}" 
    model.save(path)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='My program description')
    parser.add_argument('--data_x', type=str)
    parser.add_argument('--data_y', type=str)
    args = parser.parse_args()
    step3(args)    