'''15. 역순 연결 리스트'''

# 재귀 구조로 뒤집기
def reverseList(self, head):
    def reverse(node, prev):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)


# 반복 구조로 뒤집기
def reverseList(self, head):
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev