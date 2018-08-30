# 원점(0,0) 부터 출발하는 경로 함수 설정
import numpy as np


def user_path(low_x, high_x):
    path_x = np.arange(low_x, high_x, 25)
    path_y = 1/1000 * path_x * path_x
    node_coordinate = [path_x, path_y]

    return node_coordinate

