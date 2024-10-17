# Number of Palindromic Substrings
class Solution:
    def countPalindromicSubstrings(self, s : str, k : int) -> int:
        '''i,count=0,0
        while(i<=len(s)-k):
            substring=s[i:i+k]
            reversed_substring=substring[::-1]
            if(substring==reversed_substring):
                count+=1
            i+=1
        return count'''
        '''count=0
        if(k==1):
            return 0
        uniquecharlist=set([i for i in s])
        uniquecharcount={}
        for i in uniquecharlist:
            uniquecharcount[i]=s.count(i)
        #print(uniquecharcount)
        if(k%2!=0):
            evencount=0
            oddcount=0
            for i in uniquecharcount.values():
                if(i%2==0):
                    count+=1
                else:
                    oddcount+=1
            if(len(uniquecharcount)%2==0 and oddcount%2==0):
                count+=1
        return count'''
        i,count=0,0
        if(k==1):
            return len(s)
        while(i<=len(s)-k):
            substring=s[i:i+k]
            #reversed_substring=substring[::-1]
            #if(substring==reversed_substring):
                #count+=1
            uniquecharlist=set([i for i in substring])
            evencount=0
            oddcount=0
            for j in uniquecharlist:
                if(substring.count(j)%2==0):
                    evencount+=1
                else:
                    oddcount+=1
            if(evencount>=0 and oddcount<=1):
                count+=1
            #elif(oddcount)
            # elif(len(charcountdict)==1 and list(charcountdict.values())[0]>1):
            #     count+=1
            print("Subtring",substring,"Evencount",evencount,"Oddcount",oddcount,"Count",count)
            i+=1
        return count

s=Solution()
#print(s.countPalindromicSubstrings("aabb",2))
# Output = 2
print(s.countPalindromicSubstrings("addd",3))
# Output = 0