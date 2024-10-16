#Count number of words in the file

wordscount=0

with open("test.txt","r") as fileobject:
    data=fileobject.readlines()
    for i in data:
        wordslist=i.split(" ")
        wordscount+=len(wordslist)

print(f"The number of words in the file is {wordscount}.")