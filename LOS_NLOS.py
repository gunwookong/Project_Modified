# Last Modified: 18/09/17
# Needs to be modified


def los_discriminate(coordinate_bs, coordinate_ue, coordinate_bloc):
    a1_x = coordinate_bs[0], a1_y = coordinate_bs[1]
    a2_x = coordinate_ue[0], a2_y = coordinate_ue[1]

    b1_x = coordinate_bloc[0][0], b1_y = coordinate_bloc[0][1]

    b2_x = coordinate_bloc[1][0], b2_y = coordinate_bloc[1][1]

    a = 'LOS'
    b = 'None_LOS'

    node_denom = (b2_y-b1_y)*(a2_x-a1_x)-(b2_x-b1_x)*(a2_y-a1_y)
    if node_denom == 0:
        return a

    node_num_t = (b2_x-b1_x)*(a1_y-b1_y)-(b2_y-b1_y)*(a1_x-b1_x)
    node_num_s = (a2_x-a1_x)*(a1_y-b1_y)-(a2_y-a1_y)*(a1_x-b1_x)

    t = node_num_t / node_denom
    s = node_num_s / node_denom

    if t < 0 or t > 1 or s < 0 or s > 1:
        return a
    else:
        return b


"""#slope
    m = (end_of_blockage1[1] - end_of_blockage2[1]) / (end_of_blockage1[0] - end_of_blockage2[0])

    y = m * (x - end_of_blockage1[0]) + end_of_blockage1[1]
"""