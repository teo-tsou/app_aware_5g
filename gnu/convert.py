import pandas as pd


init_df = pd.read_csv('data_range_0_15.csv')

final_df = pd.read_csv('final_data.csv')


ue_init_df = pd.DataFrame(columns=['UE1','UE2','UE3'])
ue_final_df = pd.DataFrame(columns=['UE1','UE2','UE3'])

for index, row in init_df.iterrows():

    ue1 = []
    for j,item in enumerate(row):
        print(j,item)

        if j in [0,1,2]:
            # UE 1
            ue1.append(item)

        elif j in [3,4,5]:
            # UE 2
        
        elif j in [6,7,8]:
            # UE 3

    break