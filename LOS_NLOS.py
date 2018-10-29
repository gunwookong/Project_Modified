# Last Modified: 18/10/08
# Distinguish Whether Each connection between BS & UE is Line of Sight or None-Line Of Sight


def los_distinguish(filtered_coords, ue_coords):
        excel_los_nlos = []
        los_nlos = []

        for i in range(0, len(ue_coords[0])):  # Iteration: i_th UE's Location
            temp = []
            if len(filtered_coords[0][0][i]) == 0:
                """print("There is no BS within 100m radius circle")"""
            else:
                for j in range(0, len(filtered_coords[0][0][i])):  # j_th BS in i_th UE's BS sets
                    a = False
                    temp2 = "LOS"
                    for k in range(0, len(filtered_coords[1][0][0][i])):
                        node_denominator = (filtered_coords[1][2][1][i][k] - filtered_coords[1][1][1][i][k]) * (ue_coords[0][i] - filtered_coords[0][0][i][j]) - (filtered_coords[1][2][0][i][k] - filtered_coords[1][1][0][i][k]) * (ue_coords[1][i] - filtered_coords[0][1][i][j])
                        node_numerator_t = (filtered_coords[1][2][0][i][k] - filtered_coords[1][1][0][i][k]) * (filtered_coords[0][1][i][j] - filtered_coords[1][1][1][i][k]) - (filtered_coords[1][2][1][i][k] - filtered_coords[1][1][1][i][k]) * (filtered_coords[0][0][i][j] - filtered_coords[1][1][0][i][k])
                        node_numerator_s = (ue_coords[0][i] - filtered_coords[0][0][i][j]) * (filtered_coords[0][1][i][j] - filtered_coords[1][1][1][i][k]) - (ue_coords[1][i] - filtered_coords[0][1][i][j]) * (filtered_coords[0][0][i][j] - filtered_coords[1][1][0][i][k])

                        t = node_numerator_t / node_denominator
                        s = node_numerator_s / node_denominator
                        if node_denominator == 0:
                            a = False
                        elif t < 0 or t > 1 or s < 0 or s > 1:
                            a = False
                        else:
                            temp2 = "NLOS"
                            a = True
                    temp .append(temp2)
                    excel_los_nlos.append(temp2)
                    if a is True:
                        """print("LOS/NLOS 여부: %s" % temp2)"""
                    else:
                        """print("LOS/NLOS 여부: LOS")"""
            los_nlos.append(temp)
        final = [los_nlos, excel_los_nlos]
        return final
