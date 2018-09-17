# Last Modified: 18/09/17
import math
import numpy as np
import matplotlib.pyplot as plt

# To make line segment Blockage,
# Make end-Coordinates following Uniform distribution


def blockage(coordinate_blk):
    blk1_x = np.zeros(len(coordinate_blk[0]))
    blk1_y = np.zeros(len(coordinate_blk[0]))
    blk2_x = np.zeros(len(coordinate_blk[0]))
    blk2_y = np.zeros(len(coordinate_blk[0]))

    for i in range(0, len(coordinate_blk[0])):

        # Random length
        length = np.random.uniform(30, 50, 1)
        # Random angle
        angle = np.random.uniform(0, math.pi, 1)

        # make both ends' coordinates

        blk1_x[i] = (coordinate_blk[0][i] + length * math.cos(angle))
        blk1_y[i] = (coordinate_blk[1][i] + length * math.sin(angle))
        blk2_x[i] = (coordinate_blk[0][i] - length * math.cos(angle))
        blk2_y[i] = (coordinate_blk[1][i] - length * math.sin(angle))

    # Plot Line Segment Blockage for each Coordinates
    plt.plot([blk1_x, blk2_x], [blk1_y, blk2_y], color='blue')
    end_of_blk1 = [blk1_x, blk1_y]
    end_of_blk2 = [blk2_x, blk2_y]

    return end_of_blk1, end_of_blk2
