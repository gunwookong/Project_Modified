# Last Modified: 18/09/17
# Poisson point process(ppp) Generating Function
# Input: Density & Range of Area
# Output: Randomly Scattered Coordinates Following Poisson Distribution
import numpy as np


def ppp_generate(ppp_density, low_x, high_x, low_y, high_y):
    area = (high_x-low_x)*(high_y-low_y)
    pp_avg = ppp_density*area
    num_node = np.random.poisson(pp_avg, 1)

    temp_x = (np.random.uniform(low=low_x, high=high_x, size=num_node)).tolist()
    temp_y = (np.random.uniform(low=low_y, high=high_y, size=num_node)).tolist()

    node_coordinate = [temp_x, temp_y]
    return node_coordinate
