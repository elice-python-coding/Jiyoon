'''16. 두 수의 덧셈'''

# 내 풀이(틀림)
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """  
        while l1 is not None:
            if l1.val + l2.val < 9:
                if ten == 1:
                    result.val = l1.val + l2.val + 1
                    ten = 0
                else:
                    result.val = l1.val + l2.val
                
            else:
                result.val = l1.val + l2.val - 10
                ten = 1
            
            l1 = l1.next
            l2 = l2.next
            if l1  is None:
                break
            result.next = ListNode(0, None)
            result = result.next
            
        return head

# 전가산기
def addTwoNumbers(l1, l2):
    root = head = ListNode(0)

    carry = 0
    while l1 or l2 or carry:
        sum = 0
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next

        carry, val = divmod(sum + carry, 10)
        head.next = ListNode(val)
        head = head.next

    return root.next
