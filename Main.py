from Sort import lengthsort

# Sets a default path for most computers and asks the user for their own path and opens the file
Path = "C:\\"
Error = True
while Error:
    try:
        print("Enter the path for your file(" + Path +"):")
        Path = input()
        PathWithTxt = Path + "\\Sort Me.txt"
        PathWithTxt.replace("\\", "\\\\")
        file = open(PathWithTxt, "r")
        Error = False
    except:
        print("File does not exist or path invalid.")
        print()
        Error = True

# Gets the file contents and tells the user what is currently in the file and puts it in an list for ease of access
if file.mode == 'r':
    contents = file.readlines()
    NameList = []
    # Prints the contents of the file while adding the name to a list
    print("Contents in folder are: ")
    for Names in contents[1:]:
        CurrName = Names.replace(" ", "")
        print(CurrName)
        NameList.append(CurrName[0:len(CurrName)-1])
    file.close()
    # Using Python Sort you can sort alphabetically easily then sort using my method in Sort.py
    NameList.sort()
    NameList = lengthsort(NameList)

    # Prints the names in the list for the user to see sorted.
    print()
    print("The names sorted are: ")
    for Names in NameList:
        print(Names + "\n")
    # Attempts to save the sorted list of names in the same place as the text file needing to be sorted.
    try:
        Path = Path + "\\Sorted.txt"
        FileOut = open(Path, "w+")
        for Names in NameList:
            FileOut.write(Names +"\n")
        print("Sorted file exported to " + Path)
    except:
        print("Could not export into text file.")
