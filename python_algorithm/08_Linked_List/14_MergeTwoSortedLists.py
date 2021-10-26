'''14. 두 정렬 리스트의 병합'''

# 재귀 구조로 연결
def mergeTwoLists(self, l1, l2):
    # 연산자 우선 순위: '>' -> 'not' -> 'and' -> 'or'
    if not(l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = self.mergeTwoLists(l1.next, l2)
    return l1