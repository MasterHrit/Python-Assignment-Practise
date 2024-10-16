#Count the frequency of given string in the file case-insensitive

s=input("Enter the string :")
stringcount=0

with open("test.txt","r") as fileobject:
    data=fileobject.readlines()
    for i in data:
        lower_string=i.lower()
        stringcount+=lower_string.count(s.lower())

print(f"Count of string \"{s}\" in the file is {stringcount}.")
