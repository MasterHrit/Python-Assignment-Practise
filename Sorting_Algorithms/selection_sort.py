#Selection Sort

def selectionSort(arr: list[int]) -> list[int]:
    """selectionSort Function to Sort the Array in Ascending Order using Selection Sort Algorithm

    Args:
        arr (list[int]): Array list that is needed to be sorted

    Returns:
        list[int]: Sorted Array is returned
    """
    for i in range(len(arr)):
        minvalue: int=min(arr[i:])
        minindex: int=arr.index(minvalue)
        if(arr[i]>minvalue):
            arr[i],arr[minindex]=arr[minindex],arr[i]
    return arr

def main() -> None:
    arrstring: str=input("Enter the space separated array values :")
    arrlist: list[int]=[int(i) for i in arrstring.split(" ")]
    print(*selectionSort(arrlist),sep=", ",end=".")

if(__name__=="__main__"):
    main()