'''
第二十题有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。

示例 1：

输入：s = "()"
输出：true
示例 2：

输入：s = "()[]{}"
输出：true
示例 3：
输入：s = "(]"
输出：false

提示：
1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成
'''

class Solution:

    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
                continue
            else:
                if not stack:
                    return False
                if i == ')' and stack[-1] != '(':
                    return False
                if i == '}' and stack[-1] != '{':
                    return False
                if i == ']' and stack[-1] != '[':
                    return False
                stack.pop()
        if stack:
            return False
        return True
'''最快的方法
class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n == 0 or n % 2:
            return False
        
        result = []
        for i in range(n):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                result.append(s[i])
            else:
                if not result:  # 检查是否为空
                    return False
                
                if s[i] == ")" and result[-1] != "(":
                    return False
                elif s[i] == "]" and result[-1] != "[":
                    return False
                elif s[i] == "}" and result[-1] != "{":
                    return False
                
                result.pop()  # 直接使用pop来取出最后一个元素
        
        return not result  # 最终检查是否栈为空
'''