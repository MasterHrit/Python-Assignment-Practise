def countNegatives(grid: list[list[int]]) -> int:
    """countNegatives : Count Negative Integers in the Descending Sorted 2D Array using Binary Search

    Args:
        grid (list[list[int]]): 2D Array to check negative integers

    Returns:
        int: returns the count of negative integers in the 2D list
    """
    count: int=0
    for i in grid:
        start: int=0
        end: int=len(i)-1
        while(start<=end):
            mid: int=(end+start)//2
            if(i[mid]>=0):
                start=mid+1
            else:
                count+=end-start+1
                break
    return count

def main() -> None:
    grid: list[list[int]] = [[4, 3, 2, 1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    print(countNegatives(grid))
if(__name__=="__main__"):
    main()