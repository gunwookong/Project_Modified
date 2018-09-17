# Last Modified: 18/09/17
import math
import matplotlib.pyplot as plt

from UE_random_walk import random_walk
from PPP_Generate import ppp_generate
from Blockage import blockage

# Define Base Station and Blockage Density
BS_density = 2*math.pow(10, -6)
BLOC_density = 2*math.pow(10, -6)

# Make Random Coordinates of Base Station and Blockage
coordinate_BS = ppp_generate(BS_density, 0, 3000, 0, 3000)
plt.scatter(coordinate_BS[0], coordinate_BS[1], marker='x', color='orange', label='Base_Station')

coordinate_BLOC = ppp_generate(BLOC_density, 0, 3000, 0, 3000)
plt.scatter(coordinate_BLOC[0], coordinate_BLOC[1], marker='.', color='blue', label='Obstacle')

# Make Line-segment Blockage from coordinate_BLK
Line_BLOC = blockage(coordinate_BLOC)

# User Equipment's Random Walk
coordinate_UE = random_walk(3000, 3000, 100, 50)
plt.plot(coordinate_UE[0], coordinate_UE[1], color='gray', linewidth=1, label='User_Path')

# Function Label
plt.xlabel('x axis(m)')
plt.ylabel('y axis(m)')
plt.title('User Equipment Path with Base Station and Blockage')
plt.legend(loc='upper right')
plt.show()
