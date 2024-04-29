class Solution:
    def mySqrt(self, x: int) -> int:
        '''
             * 69. x 的平方根
     *
     * 给定一个非负整数 x ，计算并返回 x 的平方根，即实现 int sqrt(int x) 函数。
     *
     * 输入：x = 4
     * 输出：2
     *
     * 输入：x = 8
     * 输出：2
     * 解释：8 的平方根是 2.82842...，由于返回类型是整数，小数部分将被舍去。
     *
     * 提示：
     * 0 <= x <= 231 - 1
     *
     /**
     * 计算给定整数的平方根。
     *
     * @param x 待求平方根的整数。
     * @return x 的平方根。如果 x 是 0 或 1，则返回 x 本身。
        :param x:
        :return:
        '''
        """
        通过二分查找法找到整数 x 的平方根。

        参数:
        x: int - 需要求平方根的整数。

        返回值:
        int - x 的整数平方根。如果 x 是 0，则返回 0。
        """
        # 处理特殊情况：当 x 为 0 时，直接返回 0
        if x == 0:
            return 0

        # 初始化搜索范围的左右边界
        left = 1
        right = x

        # 开始二分查找
        while left <= right:
            mid = (left + right) // 2  # 计算中间值

            # 如果中间值的平方等于 x，直接返回中间值
            if mid * mid == x:
                return mid
            # 如果中间值的平方小于 x，缩小搜索范围至右半部分
            elif mid * mid < x:
                left = mid + 1
            # 如果中间值的平方大于 x，缩小搜索范围至左半部分
            else:
                right = mid - 1

        # 当没有找到精确的平方根时，返回搜索范围右边界，它是最接近的整数平方根
        return right

'''最快的方法
    def mySqrt(self, x: int) -> int:

        l = 0 
        r = x
        ans = 0

        while l<=r:

            mid = (l + r) // 2

            if mid * mid > x:
                r = mid - 1
            else:
                ans = mid
                l = mid + 1

        return ans
'''