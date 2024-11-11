def DiagonalSum(arr):
    rowlen = len(arr)
    sum =0
    for i in range(rowlen):
        sum += arr[i][i]
    return sum
arr = [[1,2,3],[4,5,6],[7,8,9]]
Totalsum = DiagonalSum(arr)
print(Totalsum)
