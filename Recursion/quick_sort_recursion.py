# Quick Sort

def pivot_position(arr):
    pivot=0
    for i in range(len(arr)-1):
        if(arr[i]<arr[len(arr)-1]):
            pivot+=1
    arr[pivot],arr[len(arr)-1]=arr[len(arr)-1],arr[pivot]
    i=0
    j=len(arr)-1
    while(arr[i]!=arr[pivot]):
        if(arr[i]<arr[pivot]):
            i+=1
            continue
        if(arr[j]>arr[pivot]):
            j-=1
            continue
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
    return pivot

def quick_sort(arr):
    if(len(arr)==0):
        return []
    if(len(arr)==1):
        return arr
    pivot=pivot_position(arr)
    left=quick_sort(arr[:pivot])
    right=quick_sort(arr[pivot+1:])
    return left+[arr[pivot]]+right

l1=[5,1,12,3,9,6]
print(pivot_position(l1))
print(l1)
print(quick_sort(l1))