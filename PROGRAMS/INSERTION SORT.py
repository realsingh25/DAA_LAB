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


def insertionsort(testlist):
    import datetime
    start_time = datetime.datetime.now()

    for i in range(1, len(testlist)):
        element = testlist[i]

        j = i-1
        while j>=0 and element<testlist[j]:
            testlist[j+1] = testlist[j]
            j-=1
        testlist[j+1] = element

    print('Tested time: ', datetime.datetime.now() - start_time)

if __name__ == '__main__':
    insertionsort(createlist())
