#insertion sort
def insertion_sort(lst :list [int]) -> list[int]:
    """insertion_sort Function to sort the array using Insertion Sort Method

    Args:
        list[int]: Array that is need to be sorted

    Returns:
        list[int]: Sorted Array is returned
    """
    if(not len(lst)):
        return lst
    sorted_section: list[int]=[]
    sorted_section.append(lst[0])
    for i in range(1,len(lst)):
        flag=0
        for j in range(len(sorted_section)):
            if(sorted_section[j]>lst[i]):
                flag=1
                sorted_section.insert(j,lst[i])
                break
        if(flag==0):
            sorted_section.append(lst[i])
    return sorted_section

def main() -> None:
    arrstring: str=input("Enter the space separated array values :")
    arrlist: list[int]=[int(i) for i in arrstring.split(" ")]
    print(*insertion_sort(arrlist),sep=", ",end=".")

if(__name__=="__main__"):
    main()