# Binary Search works only on sorted lists
def Binaryserach(arr,target):
    targetindex = None
    left = 0
    right = len(arr) -1
    while targetindex == None:
        mid = (left + right) //  2
        if left <=right:
            if arr[mid] == target:
                targetindex=mid
                return targetindex
            elif arr[mid] > target:
                right = mid-1
            elif arr[mid] < target:
                left = mid+1 
        else:
            return targetindex
arr = [1,24,8,15,23,84]
targetindex=Binaryserach(arr,16)
print(targetindex)