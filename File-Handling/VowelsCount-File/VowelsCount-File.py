#Count number of vowels in a file

countvowels=0
vowels=[]

with open("test.txt","r") as fileobject:
    data=fileobject.readlines()
    for i in data:
        s1=""
        for j in i:
            ch=j.lower()
            if(ch=='a' or ch=='e'or ch=='i' or ch=='o' or ch=='u'):
                countvowels+=1
                s1+=j
        vowels.append(s1)

print(f"Number of vowels in the files is {countvowels}.")
print(f"The found vowels are :")
for i in vowels:
    print(i)
