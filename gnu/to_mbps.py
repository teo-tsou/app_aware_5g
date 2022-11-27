import pandas as pd


init_df = pd.read_csv('data_range_0_15.csv')

final_df = pd.read_csv('final_data.csv')



new_init = (8*init_df/1000000)

new_final = (8*final_df/1000000)


new_init.to_csv('init_mbps.csv', sep=' ')

new_final.to_csv('final_mbps.csv', sep=' ')