def Binaryserach(arr,target):
    targetindex = None
    left = 0
    right = len(arr) -1
    while targetindex == None:
        mid = (left + right) //  2
        if left <=right:
            if arr[mid] == target:
                targetindex=mid
                return targetindex+1
            elif arr[mid] > target:
                right = mid-1
            elif arr[mid] < target:
                left = mid+1 
        else:
            return targetindex+1
def exponentialsearch(arr,target):
    n = len(arr)
    if target< arr[0]:
        return -1
    elif target == arr[0]:
        return 0
    right = 1
    while right < n:
        if target == arr[right]:
            return right+1
        if target > arr[right]:
            left = right
            right *=2
        else:
            return Binaryserach(arr[:right+1],target)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
result = exponentialsearch(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")