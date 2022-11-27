import pandas as pd


slices = pd.read_csv('on-demand_slices.txt')


set arrow from 0,33 to 162,33 nohead lc rgb 'red' dt 1
slices.to_csv('gnu_slices.csv', sep=' ')

