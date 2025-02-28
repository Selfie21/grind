class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = None
        previous = None
        overhead = False
        while l1 or l2 or overhead:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            register = num1 + num2

            decimal = ListNode(0)
            decimal.val = register + 1 if overhead else register
            if decimal.val >= 10:
                overhead = True
            else:
                overhead = False
            decimal.val %= 10
            if not result:
                result = decimal
            else:
                previous.next = decimal
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            previous = decimal
        return result



l12 = ListNode(2)
l14 = ListNode(4)
l13 = ListNode(3)
l12.next = l14
l14.next = l13

l25 = ListNode(5)
l26 = ListNode(6)
l24 = ListNode(4)
l25.next = l26
l26.next = l24

solution = Solution()
k = solution.addTwoNumbers(l12, l25)
print(k)