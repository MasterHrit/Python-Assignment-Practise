# Palindrome String using recursion
def is_palindrome(s):
    if(len(s)==0 or len(s)==1):
        return True
    smallAns=is_palindrome(s[1:len(s)-1])
    if(s[0]==s[len(s)-1] and smallAns==True):
        return True
    else:
        return False

print(is_palindrome("radar"))
print(is_palindrome("hello"))