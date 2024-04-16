from typing import List
'''
35. 搜索插入位置
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 O(log n) 的算法。
示例 1:
输入: nums = [1,3,5,6], target = 5
输出: 2
示例 2:
输入: nums = [1,3,5,6], target = 2
输出: 1
示例 3:
输入: nums = [1,3,5,6], target = 7
输出: 4
提示:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 为 无重复元素 的 升序 排列数组
-104 <= target <= 104
'''

class Solution:
    """
  该函数用于在有序列表中查找目标值的索引，如果目标值不存在，则返回插入位置的索引。

  参数:
  nums: 一个有序的整数列表。
  target: 需要查找的目标整数。

  返回值:
  目标值在列表中的索引，如果不存在，则返回插入位置的索引。
  """
    def searchInsert(self, nums: List[int], target: int) -> int:

        for x in range(len(nums)):
            # 判断当前元素是否等于目标值
            if nums[x] == target:
                return x
            # 当前元素大于目标值，直接返回当前位置
            elif nums[x] > target:
                return x
            # 当前元素小于目标值且已经是列表的最后一个元素，返回下一个位置
            elif nums[x] < target and x == len(nums)-1:
                return x+1

'''最快方法

    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            middle = (left + right) //2
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle -1
        return left
'''