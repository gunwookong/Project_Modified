# Last Modified: 18/10/29
# User Equipment's Random Walk Process
# Input: Range of Area, Number of Steps, Length per Step
# Output: Random Sequential Walk in Same Strides
# Random 4-way direction walk: North, South, East, West

import random
import numpy as np
import matplotlib.pyplot as plt


def random_walk_4_directions(max_x, max_y, num, step_length_per_sec):
    x = np.zeros(num)  # Generate number of steps and starting point
    y = np.zeros(num)
    x[0] = max_x/2  # Start from center of the map
    y[0] = max_y/2

    i = 1  # Counter
    a = True
    one_step = step_length_per_sec

    while i < num:
        val = random.randint(1, 4)
        if val == 1:  # One Step to the East
            x[i] = x[i - 1] + one_step
            y[i] = y[i - 1]
            # Re-run if the coordinate already has been passed or exceeds max,min range
            for j in range(1, i):
                if x[i] == x[j-1] and y[i] == y[j-1]:
                    a = False
                elif x[i] > max_x:
                    a = False
                else:
                    a = True
            if a is False:
                continue
            else:
                i = i+1

        elif val == 2:  # One Step to the West
            x[i] = x[i - 1] - one_step
            y[i] = y[i - 1]
            # Re-run if the coordinate already has been passed or exceeds max,min range
            for j in range(1, i):
                if x[i] == x[j-1] and y[i] == y[j-1]:
                    a = False
                elif x[i] < 0:
                    a = False
                else:
                    a = True
            if a is False:
                continue
            else:
                i = i + 1

        elif val == 3:  # One Step to the North
            x[i] = x[i - 1]
            y[i] = y[i - 1] + one_step
            # Re-run if the coordinate already has been passed or exceeds max,min range
            for j in range(1, i):
                if x[i] == x[j - 1] and y[i] == y[j - 1]:
                    a = False
                elif y[i] > max_y:
                    a = False
                else:
                    a = True
            if a is False:
                continue
            else:
                i = i + 1

        else:  # One Step to the South
            x[i] = x[i - 1]
            y[i] = y[i - 1] - one_step
            # Re-run if the coordinate already has been passed or exceeds max,min range
            for j in range(1, i):
                if x[i] == x[j-1] and y[i] == y[j-1]:
                    a = False
                elif y[i] < 0:
                    a = False
                else:
                    a = True
            if a is False:
                continue
            else:
                a = True
                i = i + 1

    node_x = x.tolist()
    node_y = y.tolist()
    node_coords = [node_x, node_y]
    plt.scatter(x[0], y[0], marker='d', color='blue', s=10, label='Starting point')  # Plot starting point
    plt.scatter(x[num - 1], y[num - 1], marker='s', color='red', s=10, label='Finishing point')  # Plot finishing point

    return node_coords
