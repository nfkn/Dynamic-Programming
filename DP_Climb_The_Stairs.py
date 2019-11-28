# 问题描述：
# 有个小孩上楼梯，共有N阶楼梯，小孩一次可以上1阶，2阶。走到N阶楼梯，一共有多少种走法？
import time

class DP_CTS:
    def __init__(self):
        print('begain DP')

    # 函数功能：有个小孩上楼梯，共有N阶楼梯，小孩一次可以上1阶，2阶。走到N阶楼梯，一共有多少种走法？
    #         动态规划的方法解决这类问题，动态规划方程way(N) = way(N-1) + way(N-2)
    # 动态规划方程理解为：走上第N个台阶的方法有两种：
    #      1、从第N-1个台阶跨一步到达第N个台阶；
    #      2、从第N-2个台阶跨两步到达第N个台阶。
    # 函数输入：num为楼梯的总阶数
    # 函数输出：走到N阶楼梯，总共的走法
    def climb_the_stairs_way(self, num):
        if num == 0:
            return 0
        elif num == 1:
            return 1
        elif num == 2:
            return 2
        else:
            return self.climb_the_stairs_way(num-1) + self.climb_the_stairs_way(num-2)

    # 函数功能：按照数列的方式计算，同样是way(N) = way(N-1) + way(N-2)，
    #      但是是按顺序的方式计算的，即从0、1、2开始计算。
    # 函数输入：num为楼梯的总阶数
    # 函数输出：走到N阶楼梯，总共的走法
    def fib(self, num):
        way = [index for index in range(0, num+1)]
        way[0] = 0
        way[1] = 1
        way[2] = 2
        for index in range(3, num+1):
            way[index] = way[index-1] + way[index-2]
        return way[num]

# python动态规划算法计算耗时较大，与c语言编写的动态规划相比要慢10倍左右
# 采用计算斐波拉契数列的方式非常快
if __name__ == '__main__':
    num = 45000
    DP = DP_CTS()
    time1 = time.process_time()
    # DP.climb_the_stairs_way(num)
    DP.fib(num)
    time2 = time.process_time()
    print(time2 - time1)
