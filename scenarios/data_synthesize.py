from xxlimited import new
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read data
df = pd.read_csv('data2.csv')

# drop time column
new_df = df.drop(columns=['Time','empty'],axis=1)

# implement gaussian noise
mu, sigma = 0, 0.1 # mean and standard deviation




train_df = pd.DataFrame(columns=new_df.columns)
train_df.to_csv('train_data.csv')


# how many scenarios we want to synthesize
num_synth = 300

for synth in range(num_synth):
    if synth%10==0:
        print('Progress',synth,'/',num_synth)
    # iterate through data frame
    for index, row in new_df.iterrows():
        # init new row
        new_row = []

        # iterate through row    
        for j, item in enumerate(row):

            if item == 'None':
                new_row.append(item)
                continue

            # calculate noise percentage
            noise_percentage = np.random.normal(mu, sigma, 1)[0]

            # convert str to numerical
            if isinstance(item, str):
                item = eval(item)

            # mean of the column of the item
            try:
                col_mean = np.mean(new_df.iloc[:,j])
            except:
                col_mean = item

            # apply this percentage to the item, get some proportion of the mean value of the column as a noise
            # this is done in order the noise to be equally distributed
            if item != 0:
                noised_item = round(item + noise_percentage*col_mean)
            else:
                noised_item = 0


            # be careful when noised item takes values outside of CQI range
            if j in [12,13,14]:
                if noised_item >15:
                    noised_item = 15

            # be careful when values become negative        
            if noised_item <0:
                noised_item = 0

            new_row.append(noised_item)

        
        # now that you have the new row, append it in data frame
        temp_df = pd.DataFrame(new_row).T
        temp_df.to_csv('train_data.csv', mode='a',header=False, index=False)


