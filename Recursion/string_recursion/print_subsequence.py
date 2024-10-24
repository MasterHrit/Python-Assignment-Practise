# To Print Subsequence of String using Recursion
def subsequences(s):
    if(len(s)==0):
        print("\'\'",end=" ")
        return [""]
    smallAns=subsequences(s[1:])
    for i in list(s[0]+i for i in smallAns):
        print(i,end=" ")
    return [s[0]+i for i in smallAns]+smallAns

subsequences("abc")