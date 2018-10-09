# Last Modified: 18/10/02
# At Each UE's Location, Make 100m-Radius Effective Coverage
import math


def coverage_filter(coordinate_bs, coordinate_bloc, coordinate_ue):
    eff_bs_x = []
    eff_bs_y = []
    eff_cen_bloc_x = []
    eff_cen_bloc_y = []
    eff_end1_bloc_x = []
    eff_end1_bloc_y = []
    eff_end2_bloc_x = []
    eff_end2_bloc_y = []
    radius = 100  # Radius of Coverage

    for i in range(0, len(coordinate_ue[0])):  # Iteration: i_th UE's Location
        bs_x_temp = []
        bs_y_temp = []
        bloc_x_cen_temp = []
        bloc_y_cen_temp = []
        bloc_x_end1_temp = []
        bloc_y_end1_temp = []
        bloc_x_end2_temp = []
        bloc_y_end2_temp = []

        for j in range(0, len(coordinate_bs[0])):  # Iteration: j_th Base Station at i_th UE's Location
            # Check Whether Each Base Station is within 100m Radius Circle
            if math.pow(coordinate_ue[0][i] - coordinate_bs[0][j], 2) + math.pow(
                    coordinate_ue[1][i] - coordinate_bs[1][j], 2) <= math.pow(radius, 2):

                bs_x_temp.append(coordinate_bs[0][j])
                bs_y_temp.append(coordinate_bs[1][j])

        eff_bs_x.append(bs_x_temp)
        eff_bs_y.append(bs_y_temp)

        for k in range(0, len(coordinate_bloc[0][0])):  # Iteration: k_th Blockage at i_th UE's Location
            # Check Whether Each Blockage is within 100m Radius Circle
            if (math.pow(coordinate_ue[0][i] - coordinate_bloc[0][0][k], 2) + math.pow(
                    coordinate_ue[1][i] - coordinate_bloc[0][1][k], 2) <= math.pow(radius, 2)) or (math.pow(coordinate_ue[0][i] - coordinate_bloc[1][0][k], 2) + math.pow(
                    coordinate_ue[1][i] - coordinate_bloc[1][1][k], 2) <= math.pow(radius, 2)) or (math.pow(coordinate_ue[0][i] - coordinate_bloc[2][0][k], 2) + math.pow(
                    coordinate_ue[1][i] - coordinate_bloc[2][1][k], 2) <= math.pow(radius, 2)):

                bloc_x_cen_temp.append(coordinate_bloc[0][0][k])
                bloc_y_cen_temp.append(coordinate_bloc[0][1][k])
                bloc_x_end1_temp.append(coordinate_bloc[1][0][k])
                bloc_y_end1_temp.append(coordinate_bloc[1][1][k])
                bloc_x_end2_temp.append(coordinate_bloc[2][0][k])
                bloc_y_end2_temp.append(coordinate_bloc[2][1][k])
        eff_cen_bloc_x.append(bloc_x_cen_temp)
        eff_cen_bloc_y.append(bloc_y_cen_temp)
        eff_end1_bloc_x.append(bloc_x_end1_temp)
        eff_end1_bloc_y.append(bloc_y_end1_temp)
        eff_end2_bloc_x.append(bloc_x_end2_temp)
        eff_end2_bloc_y.append(bloc_y_end2_temp)

    eff_bloc = [[eff_cen_bloc_x, eff_cen_bloc_y], [eff_end1_bloc_x, eff_end1_bloc_y], [eff_end2_bloc_x, eff_end2_bloc_y]]
    eff_bs = [eff_bs_x, eff_bs_y]
    eff_coordinate = [eff_bs, eff_bloc]

    return eff_coordinate
