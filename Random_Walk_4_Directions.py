# Last Modified: 18/09/17
import random
import numpy as np
import matplotlib.pyplot as plt

# User Equipment'Random Walk
# Input: Range of Area, Number of Steps, Length of One step
# Output: Random Sequential Walk in Even Strides


def random_walk_4_directions(max_x, max_y, num, one_step):
    # Generate number of steps and starting point
    x = np.zeros(num)
    y = np.zeros(num)
    x[0] = max_x/2
    y[0] = max_y/2

    # Plot starting point
    plt.scatter(x[0], y[0], marker='d', color='green', label='Starting point')

    # Random 4-way Direction Walk
    i = 1
    a = True
    while i < num:
        val = random.randint(1, 4)

        # One Step to the East
        if val == 1:
            x[i] = x[i - 1] + one_step
            y[i] = y[i - 1]
        # Re-run If Coordinates already have been passed or exceed maximum range
            for j in range(1, i):
                if x[i] == x[j-1] and y[i] == y[j-1]:
                    a = False
                elif x[i] > max_x:
                    a = False
                else:
                    a = True

            if a == False:
                continue
            else:
                a = True
                i = i+1

        # One Step to the West
        elif val == 2:
            x[i] = x[i - 1] - one_step
            y[i] = y[i - 1]
            for j in range(1, i):
                if x[i] == x[j-1] and y[i] == y[j-1]:
                    a = False
                elif x[i] < 0:
                    a = False
                else:
                    a = True

            if a == False:
                continue
            else:
                a = True
                i = i + 1

        # One Step to the North
        elif val == 3:
            x[i] = x[i - 1]
            y[i] = y[i - 1] + one_step
            for j in range(1, i):
                if x[i] == x[j - 1] and y[i] == y[j - 1]:
                    a = False
                elif y[i] > max_y:
                    a = False
                else:
                    a = True

            if a == False:
                continue
            else:
                a = True
                i = i + 1

        # One Step to the South
        else:
            x[i] = x[i - 1]
            y[i] = y[i - 1] - one_step
            for j in range(1, i):
                if x[i] == x[j-1] and y[i] == y[j-1]:
                    a = False
                elif y[i] < 0:
                    a = False
                else:
                    a = True

            if a == False:
                continue
            else:
                a = True
                i = i + 1

    node_x = x.tolist()
    node_y = y.tolist()
    node_coordinate = [node_x, node_y]
    plt.scatter(x[num-1], y[num-1], marker='s', color='red', label='Finishing point')

    return node_coordinate
