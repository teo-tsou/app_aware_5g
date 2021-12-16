import pandas as pd
import argparse
from pathlib import Path
import json
import numpy as np


def step2(args):
    with open(args.data) as data_file:
        data = json.load(data_file)
    df = pd.DataFrame(data)
    df = df.drop('Time',axis=1)
    print(df)
    val_X = []
    val_y = []

    # convert to list
    array = df.values.tolist()
    print(array)
    # create X and y
    X,y = extract_X_y_from_file(array, 5, 2)
    print(X,y)
    # add to final data
    val_X = val_X + X
    val_y = val_y + y

    X_val = np.array(val_X)
    print(X_val.shape)

    y_val = np.array(val_y)
    print(y_val.shape)

    list_x = list(X)
    list_y = list(y)

    print(type(list_y))
    print(type(list_y[0]))
    with open(args.out_x, 'w') as outx_file:
        json.dump(list_x, outx_file)

    with open(args.out_y, 'w') as outy_file:
        json.dump(list_y, outy_file)   


def extract_X_y_from_file(array, X_num, y_num):
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
        for j in range(9):
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
        
 

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='My program description')
    parser.add_argument('--data', type=str)
    parser.add_argument('--out_x', type=str)
    parser.add_argument('--out_y', type=str)
    args = parser.parse_args()
    Path(args.out_x).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_y).parent.mkdir(parents=True, exist_ok=True)
    step2(args)
