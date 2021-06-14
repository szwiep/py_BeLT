import numpy as np
import shelve

import plotting


# Path to run-info file
fp_in = 'run-info-202106-1411-0816-3d4d0559-afc6-483a-9034-340455de9136'
# Path to output directory
fp_out = './shelf_test/'
# Range to plot
iteration_range = [10, 30] 
# Plot height
y_limit = 10

with shelve.open(fp_in, 'r') as shelf:
    # for iter in range(iteration_range[0], iteration_range[1]+1):
    #     plotting.stream(iter, np.array(shelf["bed"]), np.array(shelf[str(iter)][0]), 
    #                     shelf["param"]["x_max"], y_limit, np.array(shelf[str(iter)][1]), fp_out)
    # plotting.flux_info(np.array(shelf["flux"]), shelf["param"]["n_iterations"], fp_out)
    # plotting.flux_info2(np.array(shelf["flux"]), np.array(shelf["avg_age"]), shelf["param"]["n_iterations"], fp_out)
    plotting.flux_info3(np.array(shelf["flux"]), np.array(shelf["avg_age"]), np.array(shelf["age_range"]), 
                        shelf["param"]["n_iterations"], fp_out)