import numpy

def arrays(arr):
    ls=[]
    for i in range(len(arr)):
        ls.append(arr[len(arr)-i-1])
    return(numpy.array(ls,float))


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
