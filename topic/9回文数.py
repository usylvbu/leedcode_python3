''' 第9题
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false
回文数
是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
例如，121 是回文，而 123 不是。
示例 1：
输入：x = 121
输出：true
示例 2：

输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3：
输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数。
提示：
-231 <= x <= 231 - 1
进阶：你能不将整数转为字符串来解决这个问题吗？
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        global count
        if x < 0 :
            return False
        count = []
        tem = x
        while int(x) > 0:
            count.append(int(x % 10))
            x /= 10
        x = tem
        length = len(count)
        if length == 1:
            return True
        elif length == 2:
            if x % 11 == 0:
                return True
            else:
                return False
        else:
            tem = 0
            while length-1 > tem:
                if count[length-1] == count[tem]:
                    length -= 1
                    tem += 1
                    continue
                else:
                    return False
        return True

''' 使用字符串的方法
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        
        # 将整数转换为字符串，并判断其是否和翻转后的字符串相等
        str_x = str(x)
        reversed_str_x = str_x[::-1]
        return str_x == reversed_str_x

'''