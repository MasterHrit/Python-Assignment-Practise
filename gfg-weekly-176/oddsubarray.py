def countoddSubarrays(n : int, arr : list[int]) -> int: # type: ignore
        # code here
        '''oddarr=set([i for i in arr if(i%2!=0)])
        evenarr=set([i for i in arr if(i%2==0)])
        return len(oddarr)*len(evenarr)'''
        i=0
        list1=[]
        subarraycount=0
        while i<len(arr):
            list1.append(arr[i])
            if(len(list1)%2!=0):
                i+=1
                continue
            oddcount=0
            #print(list1)
            for j in list1:
                if(j%2!=0):
                    oddcount+=1
            if(oddcount%2!=0):
                subarraycount+=1
                #print(len(list1),i)
                if(len(list1)-i==0):
                     break
                else:
                    i=len(list1)-i
                    list1=[]
                    continue
            i+=1
        return subarraycount
print(countoddSubarrays(8,[2,4,7,3,6,9,9,9]))