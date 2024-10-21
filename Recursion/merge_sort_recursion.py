# Merge Sort Recursion

def merge_sort(arr):
    if(len(arr)==0):
        return
    if(len(arr)==1):
        return arr
    mid=(len(arr)-1)//2
    leftsorted=merge_sort(arr[:mid+1])
    rightsorted=merge_sort(arr[mid+1:])
    returnlist=[]
    i,j=0,0
    while(i!=len(leftsorted) and j!=len(rightsorted)):
        if(leftsorted[i]>rightsorted[j]):
            returnlist.append(rightsorted[j])
            j+=1
        elif(leftsorted[i]<rightsorted[j]):
            returnlist.append(leftsorted[i])
            i+=1
        elif(leftsorted[i]==rightsorted[j]):
            returnlist.append(leftsorted[i])
            returnlist.append(rightsorted[j])
            i+=1
            j+=1
    if(i!=len(leftsorted)):
        returnlist+=leftsorted[i:]
    elif(j!=len(rightsorted)):
        returnlist+=rightsorted[j:]
    return returnlist


print(merge_sort([3, 0, 2, 5, -1, 4, 1]))