import pandas as pd


init_df = pd.read_csv('data_range_0_15.csv')

final_df = pd.read_csv('final_data.csv')



new_init = (init_df*1000)

new_final = (final_df*1000)


new_init.to_csv('init_jitter.csv', sep=' ')

new_final.to_csv('final_jitter.csv', sep=' ')
