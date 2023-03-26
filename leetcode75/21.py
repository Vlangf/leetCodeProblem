def mergeTwoLists(list1, list2):
    result = ListNode(0)
    temp = result
    while list1 and list2:
        if list1.val < list2.val:
            temp.next = list1.val
            list1 = list1.next
        else:
            temp.next = list2.val
            list2 = list2.next

        temp = temp.next

    if list1:
        temp.next = list1
    elif list2:
        temp.next = list2

    return result.next


print(mergeTwoLists(list1=[1, 2, 4], list2=[1, 3, 4]))
