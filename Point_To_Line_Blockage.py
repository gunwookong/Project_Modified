# Last Modified: 18/09/17
import math
import numpy as np
import matplotlib.pyplot as plt

# To Make Line Segment Blockage,
# Make Both Ends'-Coordinates are following Uniform distribution


def line_blockage_generate(coordinate_center_bloc):
    bloc1_x = np.zeros(len(coordinate_center_bloc[0]))
    bloc1_y = np.zeros(len(coordinate_center_bloc[0]))
    bloc2_x = np.zeros(len(coordinate_center_bloc[0]))
    bloc2_y = np.zeros(len(coordinate_center_bloc[0]))

    for i in range(0, len(coordinate_center_bloc[0])):

        # Unit Random Blockage Length (min, max, num) Follows Uniform Distribution
        length = np.random.uniform(30, 100, 1)
        # Random Blockage angle (min, max, num) Also Follows Uniform Distribution
        angle = np.random.uniform(0, math.pi, 1)

        # make both ends' coordinates
        bloc1_x[i] = (coordinate_center_bloc[0][i] + length * math.cos(angle))
        bloc1_y[i] = (coordinate_center_bloc[1][i] + length * math.sin(angle))
        bloc2_x[i] = (coordinate_center_bloc[0][i] - length * math.cos(angle))
        bloc2_y[i] = (coordinate_center_bloc[1][i] - length * math.sin(angle))

    # Plot Line Segment Blockage for each Coordinates
    plt.plot([bloc1_x, bloc2_x], [bloc1_y, bloc2_y], color='blue')
    end_of_bloc1_x = bloc1_x.tolist()
    end_of_bloc1_y = bloc1_y.tolist()
    end_of_bloc2_x = bloc2_x.tolist()
    end_of_bloc2_y = bloc2_y.tolist()
    end_of_bloc1 = [end_of_bloc1_x, end_of_bloc1_y]
    end_of_bloc2 = [end_of_bloc2_x, end_of_bloc2_y]
    coordinate_line_blockage = [coordinate_center_bloc, end_of_bloc1, end_of_bloc2]

    return coordinate_line_blockage
