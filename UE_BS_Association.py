# Last Modified: 18/10/10
# User Equipment Should Be Connected with Base Station which has the Lowest Pathloss Value at Each Location


def association(ue_coords, pathloss_val, filtered_coords):
    min_pathloss_log = []
    bs_index_log = []
    bs_x_log = []
    bs_y_log = []

    for m in range(0, len(ue_coords[0])):
        if len(pathloss_val[0][m]) == 0:
            min_pathloss_log.append('NULL')
            bs_index_log.append('NULL')
            bs_x_log.append('NULL')
            bs_y_log.append('NULL')

        else:
            for k in range(0,pathloss_val[0][m])
                pathloss_val[0]
            min_pathloss_log.append(min(pathloss_val[0][m]))
            for n in range(0, len(pathloss_val[0][m])):
                if min(pathloss_val[0][m]) == pathloss_val[0][m][n]:
                        bs_index_log.append(filtered_coords[2][m][n])
                        bs_x_log.append(filtered_coords[0][0][m][n])
                        bs_y_log.append(filtered_coords[0][1][m][n])
                        break

    hand_over_count = 0
    for j in range(0, len(bs_index_log)-1):
        if bs_index_log[j+1] == bs_index_log[j]:
            hand_over_count += 0
        elif bs_index_log[j+1] != bs_index_log[j]:
            hand_over_count += 1

    excel_hand_over = [hand_over_count]

    assn_info = [min_pathloss_log, bs_x_log, bs_y_log, bs_index_log, excel_hand_over]
    return assn_info



