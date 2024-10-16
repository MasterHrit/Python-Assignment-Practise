#Bubble Sort

def bubbleSort(arr: list[int]) -> list[int]:
    """bubbleSort Function to Sort the Array using Bubble Sort Algorithm

    Args:
        arr (list[int]): Array to be sorted

    Returns:
        list[int]: Sorted Array is returned
    """
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
def main() -> None:
    arrstring: str=input("Enter the space separated array values :")
    arrlist: list[int]=[int(i) for i in arrstring.split(" ")]
    print(*bubbleSort(arrlist),sep=", ",end=".")

if(__name__=="__main__"):
    main()