#Count the number of characters in a file
countletters=0
with open("test.txt","r") as fileobject:
    data: list[str]=fileobject.readlines()
    for i in data:
        for j in i:
            if(j!="\n"):
                countletters+=1
print(f"No. of letters in the file is {countletters}.")
'''
def read_functionality() -> None:
    with open("test.txt","r") as  fileobject:
        data: str=fileobject.read()
        print(data)

read_functionality()
'''