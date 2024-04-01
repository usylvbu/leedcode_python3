from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = [0, 1]
        a = 0
        b = 0
        for i in nums:
            b = a + 1
            for j in nums[b:]:
                if i + j == target:
                    result[0] = a
                    result[1] = b
                    return result
                else:
                    b += 1
            a += 1
        return result