
#Sort the names by length using bubblesort
def lengthsort(NameList):
    for Names in NameList[0:-1]:
        for CurrName in NameList[0:-1]:
            CurrNameIndex = NameList.index(CurrName)
            if len(CurrName) > len(NameList[CurrNameIndex+1]):
                NameList[CurrNameIndex], NameList[CurrNameIndex+1] = NameList[CurrNameIndex+1], NameList[CurrNameIndex]
    return NameList


#def alphabeticalsort(NameList):
