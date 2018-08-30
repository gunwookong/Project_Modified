import numpy as np


def ppp_generate(ppp_density, low_x, high_x, low_y, high_y):
    area = (high_x-low_x)*(high_y-low_y)
    pp_avg = ppp_density*area
    num_node = np.random.poisson(pp_avg, 1)
    tmp_x = np.random.uniform(low=low_x, high=high_x, size=num_node)
    tmp_y = np.random.uniform(low=low_y, high=high_y, size=num_node)

    node_coordinate = [tmp_x, tmp_y]
    return node_coordinate
