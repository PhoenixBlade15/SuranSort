from Sort import lengthsort

#Gets the file contents and tells the user what is currently in the file and puts it in an list for ease of access
file = open("C:\\Users\\Matthew\\Desktop\\SuranSort\\SuranSort\\Sort Me.txt", "r")
if file.mode == 'r':
    contents = file.readlines()
    NameList = []
    print("Contents in folder are: ")
    for Names in contents[1:]:
        CurrName = Names.replace(" ", "")
        print(CurrName)
        NameList.append(CurrName[0:len(CurrName)-1])
    NameList = lengthsort(NameList)
    print(NameList)

#input()
