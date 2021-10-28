'''k개 정렬 리스트 병합'''

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
        heap.sort()
        
        if len(heap) == 0:
            return None
        
        head = ListNode(heap[0])
        result = head
        for i in range(1, len(heap)):
            result.next = ListNode(heap[i])
            result = result.next
            
        return head