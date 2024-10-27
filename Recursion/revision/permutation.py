# Return List containing all permutations of the string
def return_permutations(str1):
    if(len(str1)==0):
        return [""]
    l1=[]
    firstchar=str1[0]
    restString=str1[1:]
    smallAns=return_permutations(restString)
    for i in smallAns:
        for j in range(len(i)+1):
            l1.append(i[:j]+firstchar+i[j:])
    return l1

s1="ab"
print(return_permutations(s1))