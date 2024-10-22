# Remove_Character using recursion

def remove_character(s1,ch):
    if(len(s1)==0):
        return ""
    smallAns=remove_character(s1[1:],ch)
    if(s1[0]==ch):
        return smallAns
    else:
        return s1[0]+smallAns

s1="dragon ball z"
print(remove_character(s1,"z"))