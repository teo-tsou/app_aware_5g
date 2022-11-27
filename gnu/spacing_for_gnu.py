import pandas as pd


init_df = pd.read_csv('data_range_0_15.csv')

final_df = pd.read_csv('final_data.csv')


init_df.to_csv('init_spacing.csv', sep=' ')

final_df.to_csv('final_spacing.csv', sep=' ')
