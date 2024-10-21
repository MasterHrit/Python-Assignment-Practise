# Binary Search Using Recursion

def Binary_Search_Using_Recursion(arr, element):
    if(len(arr)==0):
        return False
    mid=(len(arr)-1)//2
    if(arr[mid]==element):
        return True
    elif(arr[mid]>element):
        return Binary_Search_Using_Recursion(arr[:mid],element)
    elif(arr[mid]<element):
        return Binary_Search_Using_Recursion(arr[mid+1:],element)

print(Binary_Search_Using_Recursion([3, 5, 1, 7, 9],25))