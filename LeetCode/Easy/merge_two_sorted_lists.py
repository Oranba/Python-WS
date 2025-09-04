from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def MergeTwoLists(self,list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    current = ListNode()
    if not list1:
     return list2
    if not list2:
     return list1
        
    if list1.val < list2.val or list1.val==list2.val:
     current.val= list1.val
     current.next = self.mergeTwoLists(list1.next,list2)
    elif list1.val > list2.val:
     current.val=list2.val
     current.next=self.mergeTwoLists(list1, list2.next)

    return current

def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def test_merge_two_sorted_lists():
    # Test 1: Both lists have elements
    l1 = create_linked_list([1, 2, 4])
    l2 = create_linked_list([1, 3, 4])
    result = linked_list_to_list(MergeTwoLists(l1, l2))
    assert result == [1, 1, 2, 3, 4, 4], f"Test 1 failed: {result}"

    # Test 2: One list is empty
    l1 = create_linked_list([])
    l2 = create_linked_list([0])
    result = linked_list_to_list(MergeTwoLists(l1, l2))
    assert result == [0], f"Test 2 failed: {result}"

    # Test 3: Both lists are empty
    l1 = create_linked_list([])
    l2 = create_linked_list([])
    result = linked_list_to_list(MergeTwoLists(l1, l2))
    assert result == [], f"Test 3 failed: {result}"

    # Test 4: Lists with negative and positive numbers
    l1 = create_linked_list([-3, 5, 7])
    l2 = create_linked_list([-2, 6, 8])
    result = linked_list_to_list(MergeTwoLists(l1, l2))
    assert result == [-3, -2, 5, 6, 7, 8], f"Test 4 failed: {result}"

    print("All tests passed!")
if __name__ == "__main__":
    test_merge_two_sorted_lists()
    
    # dummy = ListNode()
    # current = dummy
    # while l1 and l2:
    #     if l1.val < l2.val:
    #         current.next = l1
    #         l1 = l1.next
    #     else:
    #         current.next = l2
    #         l2 = l2.next
    #     current = current.next

    # current.next = l1 if l1 else l2
    # return dummy.next