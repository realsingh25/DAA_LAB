def createlist():
    testlist = list()
    file = open("D:\\COLLEGE\\III YEAR\\DAA_LAB\\TEST DATA/descending.txt","r")
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

        for j in range(0, i):
            if element < testlist[j]:
                flag = len(testlist)-j-1
                while flag>=0:
                    testlist[flag+1] = testlist[]
                    flag-=1
                testlist[j] = element

    print(testlist)
    print('Tested time: ', datetime.datetime.now() - start_time)

if __name__ == '__main__':
    insertionsort(createlist())
