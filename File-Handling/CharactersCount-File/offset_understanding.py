#Offset Understanding

with open("test.txt","a+") as fileobject:
    fileobject.seek(0,0)
    data: str=fileobject.read()
    print(data)
