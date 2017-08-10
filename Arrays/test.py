# def twoSum(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#
#     dict = {}
#     i = 0
#     for item in nums:
#         dict[item] = i
#         i += 1
#     index = 0
#     i = 0
#     flag = False
#     for item in nums:
#         if (target - item) in dict:
#             index = dict[target - item]
#             if index == i:
#                 i += 1
#                 continue
#             flag = True
#             break
#         i += 1
#     if flag:
#         print (index, i)
#
# nums = [-1,-2,-3,-4,-5]
# target = -8
# twoSum(nums,target)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers( l1, l2):
    """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    ans = None
    itr = ans
    carry = 0
    while l1 is not None and l2 is not None:
        val = (l1.val + l2.val + carry)%10
        carry = (l1.val + l2.val + carry) / 10
        if ans is None:
            ans = ListNode(val)
            itr = ans
            l1 = l1.next
            l2 = l2.next
        else:
            itr.next = ListNode(val)
            itr = itr.next
            l1 = l1.next
            l2 = l2.next

    while l1 is not None:
        val = (l1.val + carry) % 10
        carry = carry = (l1.val + carry)/10
        itr.next = ListNode(val)
        itr = itr.next
        l1 = l1.next
    while l2 is not None:
        val = (l2.val + carry) % 10
        carry = carry = (l2.val + carry) / 10
        itr.next = ListNode(val)
        itr = itr.next
        l2 = l2.next
    if carry != 0:
        itr.next = ListNode(carry)
    return ans

l1 = ListNode(5)
# l1.next = ListNode(4)
# l1.next.next = ListNode(9)
# l1.next.next.next = ListNode(9)

l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)

l3 = addTwoNumbers(l1,l2)
while l3 is not None:
    print l3.val
    l3 = l3.next