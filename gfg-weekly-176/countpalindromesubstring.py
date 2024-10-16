def countPalindromicSubstrings(s : str, k : int) -> int:
    i=0
    count=0
    while((i+k)<=len(s)):
        string: str=s[i:i+k]
        '''if(i==0):
            reversestring: str=s[(i+k-1)::-1]
        else:
            reversestring=s[i+k-1:i-1:-1]
        print(string,reversestring)
        if(string==reversestring):
            print(string)
            count+=1
        i+=1'''
        '''s1=set([j for j in string])
        evencount=0
        oddcount=0
        for j in s1:
            if(string.count(j)%2==0):
                evencount+=1
            else:
                oddcount+=1
        #print(evencount,oddcount)
        if(k%2==0):
            if(evencount!=0 and oddcount==0):
                count+=1      
        else:
            if(oddcount%2==1):
                count+=1
        i+=1'''
    return count

print(countPalindromicSubstrings("abcde",3))