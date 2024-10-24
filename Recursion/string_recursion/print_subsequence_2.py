# Print Subsequence using Recursion method 2

def print_subsequence_helper(s1,takensofar):
    if(len(s1)==0):
        if(takensofar==""):
            print("\'\'")
        else:
            print(takensofar)
        return
    print_subsequence_helper(s1[1:],takensofar+s1[0])
    print_subsequence_helper(s1[1:],takensofar)

def print_subsequence(s1):
    print_subsequence_helper(s1,"")

def main():
    print_subsequence("abc")

if(__name__=="__main__"):
    main()