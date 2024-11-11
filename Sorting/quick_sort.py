def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: arrays with 0 or 1 element are already sorted
    else:
        pivot = arr[len(arr) // 2]  # Choose the pivot
        print(pivot)
        left = [x for x in arr if x < pivot]  # Elements less than the pivot
        print(left)
        middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
        print(middle)
        right = [x for x in arr if x > pivot]  # Elements greater than the pivot
        print(right)
        return quick_sort(left) + middle + quick_sort(right)  # Recursively sort and combine

# Example usage
my_list = [64, 25, 12, 22, 11]
sorted_list = quick_sort(my_list)
print(sorted_list)
