# Find all Subsequence of String

def subsequences(s):
    if(len(s)==0):
        return [""]
    smallAns=subsequences(s[1:])
    return [s[0]+i for i in smallAns]+smallAns

print(subsequences("abc"))