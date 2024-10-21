# Linear Search Using Recursion

def linearSearchUsingRecursion(arr,element):
    if(len(arr)==0):
        return False
    smallAns=linearSearchUsingRecursion(arr[1:],element)
    if(element==arr[0] or smallAns==1):
        return True
    else:
        return False
    
print(linearSearchUsingRecursion([],1))