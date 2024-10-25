#Print Permutation in String

def permutations_helper(s,takensofar,l1):
    if(len(s)==0):
        l1.append(takensofar)
        return
    firstchar=s[0]
    reststring=s[1:]
    for i in range(len(takensofar)+1):
        #taken sofar should not be manipulated it will be required for the next iteration
        newtaken=takensofar[:i]+firstchar+takensofar[i:]
        permutations_helper(reststring,newtaken,l1)

def permutations(s):
    l1=[]
    permutations_helper(s,"",l1)
    return l1

def main():
    s="abc"
    print(permutations(s))

if(__name__=="__main__"):
    main()