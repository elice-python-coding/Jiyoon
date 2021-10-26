'''18. 홀짝 연결 리스트'''

class Solution:
    def oddEvenList(self, head):
        if head is None:
            return head

        odd = head
        even = head.next
        even_head = head.next
        
        while odd and odd.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
            
        odd.next = even_head
        return head