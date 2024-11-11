def linearsearch(arr,target):
    n = len(arr)
    targetindex = None
    for i in range(0,n):
        if arr[i] == target:
            targetindex = i
            break
    if targetindex != None:
        print(targetindex)
    else:
        print("The target element is not in the Array")
arr = [1,2,4,7,6,9]
linearsearch(arr,8)