# Last Modified: 18/10/08
import math


def pathloss_calculate(scenario, filtered_coords, ue_coords, los_nlos):
    # UMa(Urban Macro cellular) Path_loss value Modeling function
    if scenario == "uma":
        # Set Fixed Values
        h_ut = 1.5  # User Equipment Height
        h_bs = 25  # Base Station Height
        h_e = 1  # Effective Environment Height
        h_prime_bs = h_bs - h_e  # Effective User Equipment Height
        h_prime_ut = h_ut - h_e  # Effective Base Station Height
        c = 3 * math.pow(10, 8)  # Propagation Velocity In Free Space
        f_c = 28 * math.pow(10, 9)  # Centre Frequency(Hz)
        d_prime_bp = 4 * h_prime_bs * h_prime_ut * f_c / c
        path_loss = []

        for i in range(0, len(ue_coords[0])):  # Iteration: Set of BSs Corresponding to i_th UE
            temp = []
            for j in range(0, len(filtered_coords[0][0][i])):  # Iteration: j_th BS in i_th Set of BS
                # Calculate Parameters
                d_2d = math.sqrt(math.pow(filtered_coords[0][0][i][j] - ue_coords[0][i], 2) + math.pow(filtered_coords[0][1][i][j] - ue_coords[1][i], 2))
                d_3d = math.sqrt(math.pow(h_bs - h_ut, 2) + math.pow(d_2d, 2))

                # Calculate Pathloss/uma/Line of Sight/
                if 10 <= d_2d <= d_prime_bp:
                    pl1 = 32.4 + 20 * math.log10(d_3d) + 20 * math.log10(f_c)
                    pl_uma_los = pl1

                elif d_prime_bp <= d_2d <= 5000:
                    pl2 = 32.4 + 40 * math.log10(d_3d) + 20 * math.log10(f_c) - 10 * math.log10(math.pow(d_prime_bp, 2) + math.pow(h_bs - h_ut, 2))
                    pl_uma_los = pl2

                # Different Path Loss Value According to LOS/NLOS
                if los_nlos[i][j] == "LOS":
                    temp.append(pl_uma_los)

                elif los_nlos[i][j] == "NLOS" and 10 <= d_2d <= 5000:
                    pl_prime_nlos = 13.54 + 39.08 * math.log(d_3d) + 20 * math.log10(f_c) - 0.6 * (h_ut - 1.5)
                    pl_uma_nlos = max(pl_uma_los, pl_prime_nlos)
                    temp.append(pl_uma_nlos)

            path_loss.append(temp)
        print("LOS/NLOS \n", los_nlos)
        print("Path Loss Value \n", path_loss)

    # UMi(Urban Micro cellular)

        # UMi- street Canyon
        #  pl_umi_los



