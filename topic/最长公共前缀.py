from typing import List
'''
14.最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
示例 1：
输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。

提示：
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]
        for s in strs:
            while len(result) > 0:
                if not s.startswith(result):
                    result = result[:-1]
                    if len(result) == 0:
                        return ""
                else:
                    break


        return result

    #最快的算法
'''
def longestCommonPrefix(self, strs: List[str]) -> str:
       if not strs or not len(strs):
           return ""
       
       def helper(len):
           str1 = strs[0][:len]
           for i in strs[1:]:
               if i[:len] != str1:
                   return False
           return True
       
       ml = min([len(i) for i in strs])
       lo = 1
       hi = ml
       
       while lo <= hi:
           mid = lo + (hi-lo)//2
           if helper(mid):
               lo = mid+1
           else:
               hi = mid-1
       return strs[0][:(lo+hi)//2]
'''