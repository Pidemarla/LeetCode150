def selectionsort(list):
    n = len(list)
    for i in range(0, n):
        min_index = i
        for j in range(i+1, n):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index] , list[i]
    return list
list1 = [5,4,3,2,1]
selectionsort(list1)
print(list1)