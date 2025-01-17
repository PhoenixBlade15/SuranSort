import inspect
import sys

# False will be default, test.bat changes this to true to test descending order
Descending = False
for arg in sys.argv:
    if arg == "True":
        Descending = True
        break
    if arg == "False":
        break

# Sets a default path for most computers and asks the user for their own path and opens the file
Path = inspect.stack()[0][1]
Path = Path.replace("Main.py", "Sort Me.txt")

Error = True
try:
    file = open(Path, "r")
    Error = False
except:
    print("File does not exist or path invalid.")
    print()
    Error = True

# Exits when an Error occurs with code of 1
if Error:
    exit(1)

# Gets the file contents and tells the user what is currently in the file and puts it in an list for ease of access
if file.mode == 'r':
    contents = file.readlines()
    NameList = []

    # Prints the contents of the file while adding the name to a list
    for Names in contents[1:]:
        CurrName = Names.strip()
        NameList.append(CurrName)
    file.close()

    # Using Python Sort you can sort alphabetically easily then sort using my method in Sort.py
    NameList.sort()
    NameList.sort(reverse = Descending, key=len)

    # Attempts to save the sorted list of names in the same place as the text file needing to be sorted.
    try:
        if Descending:
            Path = Path.replace("Sort Me.txt", "SortedR.txt")
        else:
            Path = Path.replace("Sort Me.txt", "Sorted.txt")
        FileOut = open(Path, "w")
        for Names in NameList:
            FileOut.write(Names +"\n")
        print("Sorted file exported to " + Path.replace("\\\\", "\\"))
    except:
        print("Could not export into text file.")
print()

# Hold the viewing window open so user can see the final outputs of the program
FileOut.close()
