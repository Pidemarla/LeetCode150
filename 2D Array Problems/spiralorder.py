def Spiralorder(arr):
    top, left, right, bottom = 0, 0, len(arr[0])-1, len(arr)-1
    result=[]
    while top<=bottom and left <=right:
        for i in range(left,right+1):
            result.append(arr[top][i])
        top +=1
        for i in range(top,bottom+1):
            result.append(arr[i][right])
        right -=1
        if top<=bottom:
            for i in range(right,left-1,-1):
                result.append(arr[bottom][i])
            bottom -=1
        if left<=right:
            for i in range(bottom,top-1,-1):
                result.append(arr[i][left])
            left +=1
    return result
arr = [[1,2,3],[4,5,6],[7,8,9]]
SO = Spiralorder(arr)
print(SO)   