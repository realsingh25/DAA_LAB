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


def selectionsort(testlist):
    import datetime
    start_time = datetime.datetime.now()

    for i in range(len(testlist)):
        for j in range(i+1, len(testlist)):
            if testlist[i] > testlist[j]:
                testlist[j], testlist[i] = testlist[i], testlist[j]

    print('Tested time: ', datetime.datetime.now() - start_time)

if __name__ == '__main__':
    selectionsort(createlist())
