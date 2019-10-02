def createlist():
    testlist = list()
    file = open("D:\\COLLEGE\\ACADEMIC\\III YEAR\\DAA_LAB\\TEST DATA\\descending.txt","r")
    count = 0
    for i in file:
        testlist.append(int(i))
        count += 1

        if count == 1000:
            break
    file.close()
    return testlist


def binarysearch(testlist, low, high, element, count):
    print(testlist, low, high, element, count)

    if high >= low:
        mid = (low + high)//2
        if testlist[mid] == element:
            return count
        elif testlist[mid] > element:
            return binarysearch(testlist, low, mid-1, element, count+1)
        elif testlist[mid] < element:
            return binarysearch(testlist, mid+1, high, element, count+1)
    else:
        return -1


if __name__ == '__main__':
    testlist = createlist()
    comparison = binarysearch(testlist, 0, len(testlist)-1, 99037, 0)
    print('COMPARISON: ',comparison)
