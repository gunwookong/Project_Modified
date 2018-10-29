# Last Modified: 18/10/25
# Main Function: Input-Values & Functions to Run Simulator

import math
import xlsxwriter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Poisson_Point_Process import ppp_generate
from tkinter import *
from tkinter import ttk
from Random_Walk_4_Directions import random_walk_4_directions
from Random_Walk_All_Directions import random_walk_all_directions
from Point_To_Line_Blockage import line_blockage_generate
from Radius_Of_Coverage import coverage_filter
from LOS_NLOS import los_distinguish
from Pathloss_Value import pathloss_calculate
from UE_BS_Association import association

# Default Parameters to Run Simulator
"""-----------------------------------------------------------------------------------------------------------------"""
scenario_val = 'UMa'  # Scenario type
direction_val = 'All'  # User Random Walk Direction
bs_density_val = 2*math.pow(10, -4) # Base Station Density = 10^-3
bloc_density_val = 2*math.pow(10, -5)  # Blockage Density = 10^-4
num_steps_val = 10000  # Number of User Equipment's Steps
user_velocity_val = 10  # 10 meter per sec 1,5,10
time_interval_val = 1  # 1 sec
save_file_str = 'Data_1.xlsx'  # Excel file name

# Input-Box Module
"""-----------------------------------------------------------------------------------------------------------------"""


def button_pressed(input_value):  # Get Input Variables
    global scenario_val
    global bs_density_val
    global bloc_density_val
    global num_steps_val
    global user_velocity_val
    global time_interval_val
    global direction_val
    global save_file_str

    if input_value == scenario:
            scenario_val = input_value.get()
            print("Scenario Input: ", scenario_val)
    elif input_value == direction:
            direction_val = input_value.get()
            print("User Random Walk Direction:", direction_val)
    elif input_value == bs_density:
            bs_density_val = input_value.get()
            print("Base Station Density:", bs_density_val)
    elif input_value == bloc_density:
            bloc_density_val = input_value.get()
            print("Blockage Density:", bloc_density_val)
    elif input_value == num_steps:
            num_steps_val = input_value.get()
            print("Number of Steps:", num_steps_val)
    elif input_value == user_velocity:
        user_velocity_val = input_value.get()
        print("User Velocity:", user_velocity_val)
    elif input_value == time_interval:
        time_interval_val = input_value.get()
        print("Unit-Time Interval: ", time_interval_val)
    elif input_value == save_file:
        save_file_str = input_value.get()
        print("File Name: ", save_file_str)


def reset_pressed():  # Reset Variables to default
    global scenario_val
    global direction_val
    global bs_density_val
    global bloc_density_val
    global num_steps_val
    global user_velocity_val
    global time_interval_val
    global save_file_str

    scenario_val = 'UMa'
    direction_val = 'All'
    bs_density_val = math.pow(10, -3)
    bloc_density_val = math.pow(10, -4)
    num_steps_val = 10000
    user_velocity_val = 10
    time_interval_val = 1
    save_file_str = 'Data_1'
    print("All values are reset to default values")


def quit_pressed():  # Terminate simulation
    global root
    sys.exit(0)


def start_pressed():  # Start simulation
    global scenario

    if scenario_val == 'UMa' or scenario_val == 'UMi':
        global root
        root.quit()
    else:
        print("Wrong Input. Put Right Value")


root = Tk()  # Make input window
root.title("mmWave Environment Simulator")
root.geometry("400x300")

lbl_1 = Label(root, text="Scenario(UMa/UMi)", width=25)  # Scenario Window
lbl_1.grid(row=0, column=0)
scenario = ttk.Combobox(width=8, textvariable=str)
scenario.grid(row=0, column=1)
scenario['values'] = ('UMa', 'UMi')
scenario.current(0)
btn = ttk.Button(text="Input", width=5, command=lambda: button_pressed(scenario))
btn.grid(row=0, column=2)

lbl_2 = Label(root, text="User Direction", width=25)  # Direction Window
lbl_2.grid(row=1, column=0)
direction = ttk.Combobox(width=8, textvariable=str)
direction.grid(row=1, column=1)
direction['values'] = ('All', '4_Way')
direction.current(0)
btn = ttk.Button(text="Input", width=5, command=lambda: button_pressed(direction))
btn.grid(row=1, column=2)

lbl_3 = Label(root, text="Base Station Density")  # Base Station Window
lbl_3.grid(row=2, column=0)
bs_density = Entry(root, width=10)
bs_density.grid(row=2, column=1)
bs_density.insert(END, math.pow(10, -3))
btn = Button(root, text="Input", command=lambda: button_pressed(bs_density))
btn.grid(row=2, column=2)

lbl_4 = Label(root, text="Blockage Density")  # Blockage Window
lbl_4.grid(row=3, column=0)
bloc_density = Entry(root, width=10)
bloc_density.grid(row=3, column=1)
bloc_density.insert(END, math.pow(10, -4))
btn = Button(root, text="Input", command=lambda: button_pressed(bloc_density))
btn.grid(row=3, column=2)

# number of Steps
lbl_5 = Label(root, text="Number Of Steps")  # Blockage window
lbl_5.grid(row=4, column=0)
num_steps = Entry(root, width=10)
num_steps.grid(row=4, column=1)
num_steps.insert(END, 10000)
btn = Button(root, text="Input", command=lambda: button_pressed(num_steps))
btn.grid(row=4, column=2)

lbl_6 = Label(root, text="User Velocity(m/sec)")  # User velocity Window
lbl_6.grid(row=5, column=0)
user_velocity = Entry(root, width=10)
user_velocity.grid(row=5, column=1)
user_velocity.insert(END, 10)
btn = Button(root, text="Input", command=lambda: button_pressed(user_velocity))
btn.grid(row=5, column=2)

lbl_7 = Label(root, text="Time Interval(sec)")  # Time interval Window
lbl_7.grid(row=6, column=0)
time_interval = Entry(root, width=10)
time_interval.grid(row=6, column=1)
time_interval.insert(END, 1)
btn = Button(root, text="Input", command=lambda: button_pressed(time_interval))
btn.grid(row=6, column=2)

lbl_8 = Label(root, text="File_Name")  # Time interval Window
lbl_8.grid(row=7, column=0)
save_file = Entry(root, width=10)
save_file.grid(row=7, column=1)
save_file.insert(END, 'Data_1.xlsx')
btn = Button(root, text="Input", command=lambda: button_pressed(save_file))
btn.grid(row=7, column=2)

btn = Button(root, text="Quit Simulation", command=lambda: quit_pressed())  # Quit, Reset, Start Window
btn.grid(row=8, column=0)
btn = Button(root, text="Reset", command=lambda: reset_pressed())
btn.grid(row=8, column=1)
btn = Button(root, text="Start", width=10,  command=lambda: start_pressed())
btn.grid(row=8, column=2)

root.mainloop()

# Call Functions
""""-----------------------------------------------------------------------------------------------------------"""

# Make Random Coordinates of Base Station and Blockage (Density, min_x, max_x, min_y, max_y)
coordinate_BS = ppp_generate(bs_density_val, 0, 3000, 0, 3000)
bs_count = 0
bs_index = []
for i in range(0, len(coordinate_BS[0])):
    bs_index.append(bs_count)
    bs_count += 1
plt.scatter(coordinate_BS[0], coordinate_BS[1], marker='^', s=3, color='orange', label='Base Station')

coordinate_BLOC = ppp_generate(bloc_density_val, 0, 3000, 0, 3000)
plt.scatter(coordinate_BLOC[0], coordinate_BLOC[1], marker='.', s=1, color='dimgray')

# Make Line-Segment Blockage From Center Coordinates of Blockage
Line_BLOC = line_blockage_generate(coordinate_BLOC)

# User Equipment's Random Walk (max_x , max_y, number of steps, length per step)
length = user_velocity_val * time_interval_val
if direction_val == '4_Way':
    coordinate_UE = random_walk_4_directions(3000, 3000, int(num_steps_val), length)
    plt.plot(coordinate_UE[0], coordinate_UE[1], color='black', linewidth=1, label='User Path')

elif direction_val == 'All':
    coordinate_UE = random_walk_all_directions(3000, 3000, int(num_steps_val), length)
    plt.plot(coordinate_UE[0], coordinate_UE[1], color='black', linewidth=1, label='User Path')
    """plt.Circle((coordinate_UE[0], coordinate_UE[1]), 0.5, color='blue', fill=False)
    for i in range(0, len(coordinateUE[0])):
        plt.plot"""
ue_count = 0
ue_index = []
for j in range(0, len(coordinate_UE[0])):
    ue_index.append(ue_count)
    ue_count += 1

# Filtering Base Station & Blockage within 100m Radius from Each User Equipment's Location
filtered_BS_BLOC = coverage_filter(coordinate_BS, Line_BLOC, coordinate_UE)

# Check Whether LOS or N_LOS
los_checker = los_distinguish(filtered_BS_BLOC, coordinate_UE)

# Calculate Pathloss Value
path_loss = pathloss_calculate(scenario_val, filtered_BS_BLOC, coordinate_UE, los_checker)

# Hand_over Counter
association_info = association(coordinate_UE, path_loss, filtered_BS_BLOC)

# Save Data as MS Excel Format
"""
print("TEst용", filtered_BS_BLOC[3][0])
print("Test용", filtered_BS_BLOC[3][1])
print("Test용", filtered_BS_BLOC[3][2])"""
print(len(filtered_BS_BLOC[3][2]))
print(len(filtered_BS_BLOC[3][0]))
print(len(filtered_BS_BLOC[3][1]))
print(len(filtered_BS_BLOC[4][0]))
print(len(filtered_BS_BLOC[3][1]))
print(len(los_checker[1]))
print(len(path_loss[1]))
print(len(ue_index))
print(len(coordinate_UE[0]))
print(len(association_info[3]))
print(len(association_info[1]))
print(len(association_info[0]))
df1 = pd.DataFrame({'UE_index': filtered_BS_BLOC[3][2], 'UE_x_coord': filtered_BS_BLOC[3][0], 'UE_y_coord': filtered_BS_BLOC[3][1], 'BS_index': filtered_BS_BLOC[4][2], 'BS_x_coord': filtered_BS_BLOC[4][0], 'BS_y_coord': filtered_BS_BLOC[4][1], 'LOS/NLOS': los_checker[1], 'PL_Value': path_loss[1]})
df2 = pd.DataFrame({'UE_index': ue_index, 'UE_x_coord': coordinate_UE[0], 'UE_y_coord': coordinate_UE[1], 'BS_Assn_index': association_info[3], 'BS_x_coord': association_info[1], 'BS_y_coord': association_info[2], 'PL_Value': association_info[0]})
df2.index = np.arange(1, len(df2)+1)
df3 = pd.DataFrame({'BS_index': bs_index, 'BS_x_coord': coordinate_BS[0], 'BS_y_coord': coordinate_BS[1]})
df4 = pd.DataFrame({'Hand_Over_Count': association_info[4]})
writer = pd.ExcelWriter(str(save_file_str), engine='xlsxwriter')
df1.to_excel(writer, sheet_name='Total UE_BS')
df2.to_excel(writer, sheet_name='UE_BS Assn')
df3.to_excel(writer, sheet_name='Total_BS')
df4.to_excel(writer, sheet_name='Hand_Over_Count')
writer.save()

# Function Label
plt.xlabel('x axis(m)')
plt.ylabel('y axis(m)')
plt.title('User Equipments Path with Base Station and Blockage')
plt.grid()
plt.legend(loc='upper right')
plt.show()



