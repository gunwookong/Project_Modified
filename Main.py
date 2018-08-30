import math
import matplotlib.pyplot as plt
from User_Path import user_path
from PPP_Generate import ppp_generate

# Base Station and Obstacle density
BS_density = 2*math.pow(10, -5)
OBS_density = 2*math.pow(10, -4)

# function call
coordinate_BS = ppp_generate(BS_density, 0, 1000, 0, 1000)
plt.scatter(coordinate_BS[0], coordinate_BS[1], marker='x', color='orange', label='Base_Station')
coordinate_OBS = ppp_generate(OBS_density, 0, 1000, 0, 1000)
plt.scatter(coordinate_OBS[0], coordinate_OBS[1], marker='.', color='blue', label='Obstacle')

coordinate_UE = user_path(0, 1000)
plt.scatter(coordinate_UE[0], coordinate_UE[1], marker='>', color='red', label='User_Path')

# function label
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('User Equipment Path With BS & Obs')
plt.legend(loc='upper right')
plt.show()
