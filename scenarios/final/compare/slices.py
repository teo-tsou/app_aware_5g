import pandas as pd
import numpy as np

def filter_thresholds(web_rtc, sipp, web_server, jitter, cqi):
    # thresholds: 
    # 1) app: 
    #           0 (web_server), 
    #           1 (sipp), 
    #           2 (web_rtc)
    #
    # 2) length (l): 
    #           0 (l < 25000), 
    #           1     (25000 < l < 50000), 
    #           2                 (50000 < l)
    #
    # 3) jitter (j): 
    #           0 (j < 5), 
    #           1     (5 < j < 10), 
    #           2             (10 < j)
    #
    # 4) cqi (c): 
    #           0             (11 < c), 
    #           1     (9 < c < 11), 
    #           2 (c < 9)

    # 1) app
    if web_rtc > 0:
        app = 2
    elif sipp > 0:
        app = 1
    else:
        app = 0

    # 2) length
    total_sum = web_rtc + sipp + web_server
    if total_sum > 50000:
        length = 2
    elif total_sum <= 50000 and total_sum > 25000:
        length = 1
    else:
        length = 0

    # 3) jitter
    ms_jitter = jitter*1000 # convert to ms from secs
    if ms_jitter > 10:
        jitter = 2
    elif ms_jitter <= 10 and ms_jitter > 5:
        jitter = 1
    else:
        jitter = 0

    # 4) cqi
    if cqi <= 9:
        cqi = 2
    elif cqi <= 11 and cqi > 9:
        cqi = 1
    else:
        cqi = 0

    return app, length, jitter, cqi





# Implement an efficient scheduling policy:
#
# Criteria:
# a) App,  b) Throughput,  c) Jitter,  d) CQI 

# inverse scaling to the original scale 


yhat_inverse = pd.read_csv('final_data.csv')

yhat_inverse = yhat_inverse.drop(columns=['Time','empty'])



for index, row in yhat_inverse.iterrows():
    values = row.values


    # define coeffs, the weights for every criteria of the mathematical formula
    coeff_a = 4     # app
    coeff_b = 4     # throughput
    coeff_c = 4     # jitter
    coeff_d = 4     # cqi

    # Obtain predicted values for every UE
    n_ues = 3
    slices = []

    for ue in range(n_ues):
        # parse UE's throughputs
        web_rtc = values[ue + 0]
        sipp = values[ue + 1]
        web_server = values[ue + 2]

        # parse UE's jitter
        jitter = values[ue+9]

        # parse UE's CQI
        cqi = values[ue+12]

        # filter with thresholds and define the level of priority for every criteria
        app, length, jitter, cqi = filter_thresholds(web_rtc, sipp, web_server, jitter, cqi)

        # make a decision for the slice's percentage value, based on the mathematical formula
        decision = coeff_a * app + coeff_b * length + coeff_c * jitter + coeff_d * cqi + 8

        # append
        slices.append(decision)

    # In this point, all the new slice's percentages are ready
    # check if they are over 100%

    if np.sum(slices)>100:
        # calculate the percentage that exceeds 100%
        res = np.sum(slices) - 100

        # calculate the amount that should be subtracted from every slice
        subtract_ue = math.ceil(res/n_ues)

        # subtract
        for i in range(len(slices)):
            slices[i] = slices[i] - subtract_ue

    print(slices)

    # write slices in file
    f = open('on-demand_slices.txt','a')
    f.write(str(slices[0]))
    f.write(",")
    f.write(str(slices[1]))
    f.write(",")
    f.write(str(slices[2]))
    f.write("\n")    


