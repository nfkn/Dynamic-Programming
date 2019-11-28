# 问题描述：
# 有面值为1元3元5元的硬币若干枚，如何用最少的硬币凑够N元？


class DP_CA:
    def __init__(self, amount, coins):
        self.amount = amount
        self.coins = coins
        print('begain DP_CA')

    # 函数功能：有面值为1元3元5元的硬币若干枚，如何用最少的硬币凑够N元？
    #         动态规划的方法解决这类问题，动态规划方程f(N)=min(f(N-xi)+1),其中x={x|1,3,5}
    # 动态规划方程理解为：最后一次凑成N元面值的方法有三种：
    #      1、添加1元凑成N元硬币；
    #      2、添加3元凑成N元硬币；
    #      3、添加5元凑成N元硬币
    #       找出其中拼凑次数最小的方案
    # 函数输入：amount为需要拼凑的金额
    # 函数输出：面值为1元3元5元的硬币若干枚，用最少的硬币凑够N元
    def coins_amount(self, amount):
        coins = self.coins
        # 以下两个条件为优化，按照贪心算法，优先使用最大面值的硬币来拼凑金额，
        # 如果，金额可以整除面值最大的硬币，则全部使用最大面值的硬币来凑
        # 如果，金额不可以整除面值最大的硬币，则优先使用最大面值的硬币来凑，剩下的金额使用其他面值的硬币来凑
        if amount % max(coins) == 0:
            return int(amount / max(coins))
        elif amount < (self.amount - sum(coins)):
            return amount / min(coins)
        #
        elif amount in coins:
            return 1
        elif amount == 2 or amount == 4 or amount == 6 or amount == 8:
            return 2
        else:
            # 凑金额的硬币数量先取一个最大值,后面的计算有小的值就取小的值
            min_coins = amount / min(coins)
            for index in range(len(coins)):
                count = self.coins_amount(amount-coins[index]) + 1
                if count < min_coins:
                    min_coins = count
            return min_coins


if __name__ == '__main__':
    amount = 19
    coins = [1, 3, 5]
    DP = DP_CA(amount, coins)
    print(DP.coins_amount(amount))