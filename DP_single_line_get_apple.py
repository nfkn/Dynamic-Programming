# 问题描述：
# 一个矩形区域被划分为N*M个小矩形格子K，在格子(i,j)中有A[i][j]个苹果。
# 现在从左上角的格子(1,1)出发，要求每次只能向右走一步或向下走一步，最后到达(N,M)，每经过一个格子就把其中的苹果全部拿走。
# 请找出能拿到最多苹果数的路线。

import numpy as np
import numba as nb
import time


class DP_SLGA:
    def __init__(self, A):
        self.A = A
        print('begain DP_SLGA')

    # 函数功能：单线取苹果
    #         动态规划的方法解决这类问题，动态规划方程f[i][j]=max(f[i+1][j]),f[i][j+1])+A[i][j]
    # 动态规划方程理解为：通过最一步走到f[N][M]的方法有两种：
    #      1、向下走一步；
    #      2、向右走一步；
    #        找出其中可以拿到苹果最多的方案
    # 函数输入：所在的位置i,j
    # 函数输出：
    def get_apple(self, i, j, max_apple):
        if i == 0 and j == 0:
            return self.A[i][j]
        else:
            if i != 0 and j != 0:
                apple1 = self.get_apple(i - 1, j, max_apple) + self.A[i][j]
                apple2 = self.get_apple(i, j - 1, max_apple) + self.A[i][j]
                if apple1 < apple2:
                    max_apple = apple2
                else:
                    max_apple = apple1
            elif i == 0:
                max_apple = self.get_apple(i, j - 1, max_apple) + self.A[i][j]
            else:
                max_apple = self.get_apple(i - i, j, max_apple) + self.A[i][j]
        return max_apple


if __name__ == '__main__':
    begain = time.process_time()
    i, j = 15, 15
    A = np.random.permutation(np.arange(i*j)).reshape((i, j))
    print(A)
    DP = DP_SLGA(A)
    print(DP.get_apple(i-1, j-1, 0))
