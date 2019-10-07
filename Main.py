def removewhitespace( Name ):
    if len(Name) == 0:
        return ""
    while Name[0] == ' ':
        Name = Name[1, len() ]


f = open("C:\\users\\Matthew\\Desktop\\Sort me.txt", "r")
if f.mode == 'r':
    contents = f.read()
    print("Contents in folder are: ")
    print(contents)

input()
