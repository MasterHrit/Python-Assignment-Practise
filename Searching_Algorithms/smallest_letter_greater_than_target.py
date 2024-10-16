# Smallest Letter Greater than Target

def next_greatest_letter(letters, target):
    start: int=0
    end: int=len(letters)-1
    while(start<=end):
        mid: int=(start+end)//2
        if(letters[mid]>target and mid!=0):
            end=mid-1
        elif(letters[mid]<target and mid!=(len(letters)-1)):
            start=mid+1
        elif(letters[mid]==target and mid!=(len(letters)-1)):
            return letters[mid+1]
        else:
            return letters[0]

def main() -> None:
    print(next_greatest_letter(['c', 'f', 'j'],'a'))

if(__name__=="__main__"):
    main()