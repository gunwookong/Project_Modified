# Last Modified: 18/09/18
import numpy as np


def los_discriminate(coordinate_bs, coordinate_ue, line_bloc):
        a1_x = np.array(coordinate_bs[0])
        a1_y = np.array(coordinate_bs[1])
        a2_x = np.array(coordinate_ue[0])
        a2_y = np.array(coordinate_ue[1])

        b1_x = np.array(line_bloc[0][0])
        b1_y = np.array(line_bloc[0][1])
        b2_x = np.array(line_bloc[1][0])
        b2_y = np.array(line_bloc[1][1])

        for i in range(0, len(a2_x)):
            print("The %dth user equipment:(%d ,%d)" % (i, a2_x[i], a2_y[i]))
            for j in range(0, len(a1_x)):
                print("The %dth base station:(%d, %d)" % (j, a1_x[j], a1_y[j]))
                for k in range(0, len(b1_x)):
                    node_denominator = (b2_y[k] - b1_y[k]) * (a2_x[i] - a1_x[j]) - (b2_x[k] - b1_x[k]) * (a2_y[i] - a1_y[j])
                    node_numerator_t = (b2_x[k] - b1_x[k]) * (a1_y[j] - b1_y[k]) - (b2_y[k] - b1_y[k]) * (a1_x[j] - b1_x[k])
                    node_numerator_s = (a2_x[i] - a1_x[j]) * (a1_y[j] - b1_y[k]) - (a2_y[i] - a1_y[j]) * (a1_x[j] - b1_x[k])

                    t = node_numerator_t / node_denominator
                    s = node_numerator_s / node_denominator
                    if node_denominator == 0:
                        print("LOS")

                    elif t < 0 or t > 1 or s < 0 or s > 1:
                        print("LOS")

                    else:
                        print("N_LOS")





