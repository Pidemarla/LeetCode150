def insertionsort(list):
    n = len(list)
    for i in range(1, n):
        value = list[i]
        for j in range(i-1, -1,-1):
            if list[j] > value:
                list [j], list[j+1] = value, list[j]
            else:
                break
    return list
list1 = [5,4,3,2,1]
insertionsort(list1)
print(list1)