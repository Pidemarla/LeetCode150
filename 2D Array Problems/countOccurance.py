def CountOccurance(arr,val):
    rowlen = len(arr)
    collen = len(arr[0])
    count = 0
    for i in range(rowlen):
        for j in range(collen):
            if arr[i][j] == val:
                count +=1
    return count

arr = [
    [1,2,5],
    [4,5,5],
    [7,5,9]
    ]
value = 5
CountOccurance = CountOccurance(arr,value)
print(CountOccurance)