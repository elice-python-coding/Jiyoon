'''17. 페어의 노드 스왑'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 내 풀이
    def swapPairs(self, head):
        cur = head
        if not cur:
            return cur
        
        if cur.next:
            head = cur.next

        while cur and cur.next:
            next = cur.next

            cur, next = cur.next, cur
            next.next = cur.next
            cur.next = next

            cur = cur.next.next

            if next.next and next.next.next:
                next.next = next.next.next
        return head

    # 반복 구조로 스왑
    def swapPairs(self, head):
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            # b가 a(head)를 가리키도록 할당
            b = head.next
            head.next = b.next
            b.next = head

            # prev가 b를 가리키도록 할당
            prev.next = b

            # 다음번 비교를 위해 이동
            head = head.next
            prev = prev.next.next
        return root.next


# 리스트 -> 연결 리스트
def makeNode(lst):
    res = ptr = ListNode()
    for item in lst:
        ptr.next = ListNode(item)
        ptr = ptr.next

    return res.next


head = makeNode([1,2,3,4])
ans = Solution().swapPairs(head)

while ans:
    print(ans.val, end=' ')
    ans = ans.next