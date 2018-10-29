# Last Modified: 18/10/29
# At Each UE's Location, Make 100m-Radius Effective Coverage
import math


def coverage_filter(bs_coords, bloc_coords, ue_coords):
    excel_ue_x = []
    excel_ue_y = []
    excel_ue_index = []
    excel_bs_x = []
    excel_bs_y = []
    excel_bs_index = []

    eff_bs_x = []
    eff_bs_y = []
    eff_bs_index = []
    eff_cen_bloc_x = []
    eff_cen_bloc_y = []
    eff_end1_bloc_x = []
    eff_end1_bloc_y = []
    eff_end2_bloc_x = []
    eff_end2_bloc_y = []
    radius = 100  # Radius of coverage
    ue_count = 0  # UE index Counter

    for i in range(0, len(ue_coords[0])):  # Iteration: At the i_th UE's location
        bs_x_temp = []
        bs_y_temp = []
        bs_index_temp = []
        bloc_x_cen_temp = []
        bloc_y_cen_temp = []
        bloc_x_end1_temp = []
        bloc_y_end1_temp = []
        bloc_x_end2_temp = []
        bloc_y_end2_temp = []
        bs_count = 0

        for j in range(0, len(bs_coords[0])):  # Iteration: j_th BS at i_th UE's location
            # Check whether each base station is within 100m radius circle
            if math.pow(ue_coords[0][i] - bs_coords[0][j], 2) + math.pow(
                    ue_coords[1][i] - bs_coords[1][j], 2) <= math.pow(radius, 2):

                bs_x_temp.append(bs_coords[0][j])
                bs_y_temp.append(bs_coords[1][j])
                bs_index_temp.append(bs_count)
                excel_bs_x.append(bs_coords[0][j])
                excel_bs_y.append(bs_coords[1][j])
                excel_bs_index.append(bs_count)
                excel_ue_x.append(ue_coords[0][i])
                excel_ue_y.append(ue_coords[1][i])
                excel_ue_index.append(ue_count)
            bs_count += 1
        eff_bs_x.append(bs_x_temp)
        eff_bs_y.append(bs_y_temp)
        eff_bs_index.append(bs_index_temp)

        for k in range(0, len(bloc_coords[0][0])):  # Iteration: k_th Blockage at i_th UE's location
            # Check whether each Blockage is within 100m radius circle
            if (math.pow(ue_coords[0][i] - bloc_coords[0][0][k], 2) + math.pow(
                    ue_coords[1][i] - bloc_coords[0][1][k], 2) <= math.pow(radius, 2)) or (math.pow(ue_coords[0][i] - bloc_coords[1][0][k], 2) + math.pow(
                    ue_coords[1][i] - bloc_coords[1][1][k], 2) <= math.pow(radius, 2)) or (math.pow(ue_coords[0][i] - bloc_coords[2][0][k], 2) + math.pow(
                    ue_coords[1][i] - bloc_coords[2][1][k], 2) <= math.pow(radius, 2)):

                bloc_x_cen_temp.append(bloc_coords[0][0][k])
                bloc_y_cen_temp.append(bloc_coords[0][1][k])
                bloc_x_end1_temp.append(bloc_coords[1][0][k])
                bloc_y_end1_temp.append(bloc_coords[1][1][k])
                bloc_x_end2_temp.append(bloc_coords[2][0][k])
                bloc_y_end2_temp.append(bloc_coords[2][1][k])
        eff_cen_bloc_x.append(bloc_x_cen_temp)
        eff_cen_bloc_y.append(bloc_y_cen_temp)
        eff_end1_bloc_x.append(bloc_x_end1_temp)
        eff_end1_bloc_y.append(bloc_y_end1_temp)
        eff_end2_bloc_x.append(bloc_x_end2_temp)
        eff_end2_bloc_y.append(bloc_y_end2_temp)

        ue_count += 1

    eff_bloc = [[eff_cen_bloc_x, eff_cen_bloc_y], [eff_end1_bloc_x, eff_end1_bloc_y], [eff_end2_bloc_x, eff_end2_bloc_y]]
    eff_bs = [eff_bs_x, eff_bs_y]
    excel_ue = [excel_ue_x, excel_ue_y, excel_ue_index]
    excel_bs = [excel_bs_x, excel_bs_y, excel_bs_index]
    eff_coords = [eff_bs, eff_bloc, eff_bs_index, excel_ue, excel_bs]

    return eff_coords
