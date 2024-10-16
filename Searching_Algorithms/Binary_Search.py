#Binary Search
#Input Parameters are - (Sorted Array) and (target to search)

def binarySearch(arr: list[int],target: int) -> bool:
    """binarySearch Function to search for target in a sorted array using Binary Search Algorithm

    Args:
        arr (list[int]): Sorted Array
        target (int): Target which is required to be searched

    Returns:
        bool: Returns True if Target is found in the array else returns False
    """
    start: int=0
    end: int=len(arr)
    flag: int=0
    while(start<=end):
        mid: int=(start+end)//2
        if(target>arr[mid]):
            start=mid+1
        elif(target<arr[mid]):
            end=mid-1
        elif(target==arr[mid]):
            flag=1
            break
        else:
            pass
    if(flag==0):
        return False
    else:
        return True

def main() -> None:
    arrstring: str=input("Enter the Space Separated Values for Sorted Array :")
    target: int=int(input("Enter the value to search in the array :"))
    arr: list[int]=[int(i) for i in arrstring.split(" ")]
    if(binarySearch(arr,target)):
        print("Target Found!")
    else:
        print("Target Not Found")

if(__name__=="__main__"):
    main()