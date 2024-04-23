from typing import List

'''
66.加一
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。
示例1：
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。
示例 2：
输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。
示例 3：
输入：digits = [0]
输出：[1]
提示：
1 <= digits.length <= 100
0 <= digits[i] <= 9
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        对一个由整数组成的列表进行操作，将每个数字加1，直到列表中的数字都变为9。如果所有数字都变为9，则在列表前添加1。

        参数:
        - digits: 一个整数列表，代表要操作的数字序列。

        返回值:
        - 一个整数列表，为经过加1操作后的结果。
        """
        for i in range(len(digits)-1,-1,-1):  # 从列表末尾开始遍历
            if digits[i]!=9:  # 如果当前数字不等于9
                digits[i]+=1  # 将当前数字加1，并结束循环
                return digits
            else:
                digits[i]=0  # 如果当前数字是9，则将其变为0
        return [1]+digits  # 如果列表中所有数字都变为9，则在列表前添加1

        '''最快的方法
        
        digits = map(str, digits)
        digits = ''.join(digits)
        digits = int(digits)
        digits += 1
        digits = list(str(digits))
        digits = list(map(int, digits))
        return digits
        '''
