# Permutation of String

def permutations(s1):
    if(len(s1)==0):
        return ["",]
    smallAns=permutations(s1[1:])
    firstchar=s1[0]
    l1=[]
    for i in smallAns:
        for j in range(len(i)+1):
            l1.append(i[0:j]+firstchar+i[j:])
    return l1
print(permutations("abc"))