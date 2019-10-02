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


def linearsearch(testlist, element):
    for i in range(0, len(testlist)):
        if testlist[i] == element:
            return int(i)
    return -1


if __name__ == '__main__':
    index = linearsearch(createlist(), 99674)
    comparison = index + 1
    print('INDEX & COMPARISON: ', index,',',comparison)
