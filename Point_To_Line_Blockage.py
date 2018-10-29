# Last Modified: 18/10/29
# To Make Line Segment Blockage,
# Make Both Ends'-Coordinates are following Uniform distribution

import math
import numpy as np
import matplotlib.pyplot as plt


def line_blockage_generate(cen_bloc):
    bloc1_x = np.zeros(len(cen_bloc[0]))
    bloc1_y = np.zeros(len(cen_bloc[0]))
    bloc2_x = np.zeros(len(cen_bloc[0]))
    bloc2_y = np.zeros(len(cen_bloc[0]))

    for i in range(0, len(cen_bloc[0])):
        # Make unit random blockage length (min, max, size) following uniform distribution
        length = np.random.uniform(0, 85/2, 1)  # Maximum half length of blockage is 85/2
        # Random blockage angle (min, max, size) also follows uniform distribution
        angle = np.random.uniform(0, math.pi, 1)

        bloc1_x[i] = (cen_bloc[0][i] + length * math.cos(angle))  # Make both ends' coordinates
        bloc1_y[i] = (cen_bloc[1][i] + length * math.sin(angle))
        bloc2_x[i] = (cen_bloc[0][i] - length * math.cos(angle))
        bloc2_y[i] = (cen_bloc[1][i] - length * math.sin(angle))

    plt.plot([bloc1_x, bloc2_x], [bloc1_y, bloc2_y], color='dimgray', linewidth='1.2')  # Plot line segment blockages
    plt.plot([bloc1_x[0], bloc2_x[0]], [bloc1_y[0], bloc2_y[0]], color='dimgray', linewidth='1.2', label='Blockage')
    end_bloc1_x = bloc1_x.tolist()
    end_bloc1_y = bloc1_y.tolist()
    end_bloc2_x = bloc2_x.tolist()
    end_bloc2_y = bloc2_y.tolist()
    end_bloc1 = [end_bloc1_x, end_bloc1_y]
    end_bloc2 = [end_bloc2_x, end_bloc2_y]
    line_bloc_coords = [cen_bloc, end_bloc1, end_bloc2]

    return line_bloc_coords  # [0]: Cen, [1]: End1, [2]: End2
