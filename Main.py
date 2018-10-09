# Last Modified: 18/10/08
# Main Function: Input Values to Run Simulator

import math
# import tkinter
import matplotlib.pyplot as plt
from Poisson_Point_Process import ppp_generate
from Random_Walk_4_Directions import random_walk_4_directions
from Point_To_Line_Blockage import line_blockage_generate
from Radius_Of_Coverage import coverage_filter
from LOS_NLOS import los_distinguish
from Pathloss_Value import pathloss_calculate

# Define Base Station and Blockage Density
BS_density = 2*math.pow(10, -5)
BLOC_density = 2*math.pow(10, -5)

# Make Random Coordinates of Base Station and Blockage (Density, min_x, max_x, min_y, max_y)
coordinate_BS = ppp_generate(BS_density, 0, 3000, 0, 3000)
plt.scatter(coordinate_BS[0], coordinate_BS[1], marker='^', color='orange', label='Base Station')

coordinate_BLOC = ppp_generate(BLOC_density, 0, 3000, 0, 3000)
plt.scatter(coordinate_BLOC[0], coordinate_BLOC[1], marker='.', color='blue', label='Blockage')

# Make Line-Segment Blockage From Center Coordinates of Blockage
Line_BLOC = line_blockage_generate(coordinate_BLOC)

# User Equipment's 4-Way Random Walk (max_x , max_y, number of steps, length per step)
coordinate_UE = random_walk_4_directions(3000, 3000, 100, 100)
plt.plot(coordinate_UE[0], coordinate_UE[1], color='gray', linewidth=1, label='User Path')

# Filtering Base Station & Blockage within 100m Radius from Each User Equipment's Location
filtered_BS_BLOC = coverage_filter(coordinate_BS, Line_BLOC, coordinate_UE)

# Check Whether LOS or N_LOS
los_checker = los_distinguish(filtered_BS_BLOC, coordinate_UE)

# Calculate Pathloss Value
scenario = "uma"
path_loss = pathloss_calculate(scenario, filtered_BS_BLOC, coordinate_UE, los_checker)

# Function Label
plt.xlabel('x axis(m)')
plt.ylabel('y axis(m)')
plt.title('User Equipments Path with Base Station and Blockage')
plt.legend(loc='upper right')
plt.show()


