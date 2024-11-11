def bubblesort(list):
    n = len(list)
    for i in range(0, n):
        swapped = False
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                # temp = list[j+1]
                # list[j+1] = list[j]
                # list[j] = temp
                list[j], list[j+1] = list[j+1] , list[j]
                swapped = True
        if not swapped:
            break
    return list
list1 = [5,4,3,2,1]
bubblesort(list1)
print(list1)