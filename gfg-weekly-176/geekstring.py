def hasGeekSubsequence(str : str) -> bool:
    # code here
    word: list=["g","e","e","k"]
    index=0
    for i in str:
        if(i==word[index]):
            word.pop(index)
        if(len(word)==0):
            return True
    return False

print(hasGeekSubsequence("abcgeeakd"))