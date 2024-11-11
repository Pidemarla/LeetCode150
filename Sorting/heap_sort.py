def heapify(arr1,n):
    # Build a max heap
    for i in range(n //2 -1,-1,-1):
        for j in range(i,n):
            left = 2*j +1
            right = 2*j +2
            largest =j
            if left<n and arr1[left] > arr1[largest]:
                largest = left
            if right <n and arr1[right] > arr1[largest]:
                largest = right
            if largest!=j:
                arr1[j],arr1[largest] = arr1[largest],arr1[j]
                j=largest

def heap_sort(arr):
    n = len(arr)
    for i in range(n-1,0,-1):
        heapify(arr,i+1)
        arr[i],arr[0]= arr[0], arr[i]
    return arr

# Example usage
my_list = [11, 25, 24, 64, 22,95,85,96,81]
sorted_list = heap_sort(my_list)
print(sorted_list)
