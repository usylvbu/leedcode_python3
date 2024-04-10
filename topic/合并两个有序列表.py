from typing import Optional

'''
第二十一题合并两个有序列表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
示例 1：
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：

输入：l1 = [], l2 = []
输出：[]
示例 3：

输入：l1 = [], l2 = [0]
输出：[0]

提示：
两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        head = result
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            while list1 is not None or list2 is not None:
                if list1 is None and list2 is not None:
                    result = list2
                elif list2 is None and list1 is not None:
                    result = list1
                if list1.val < list2.val:
                    result.val = list1.val
                    list1 = list1.next
                else:
                    result.val = list2.val
                    list2 = list2.next

                result = result.next
        return head

''' 最快的方法
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list2.next,list1)
            return list2
'''