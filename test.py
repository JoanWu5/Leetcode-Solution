a = [[1,2,-1,-4],
    [2,3,4,5],
    [3,4,5,6],
    [6,7,8,9]]
print(a.reverse())
a[0][0],a[0][3],a[3][3],a[3][0] = a[3][0],a[0][0],a[0][3],a[3][3]
print(a)