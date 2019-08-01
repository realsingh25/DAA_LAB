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


def bubblesort(testlist):
    import datetime
    start_time = datetime.datetime.now()

    for i in range(len(testlist)): 
        swap = False

        for j in range(0, len(testlist)-i-1): 
            if testlist[j] > testlist[j+1]: 
                testlist[j], testlist[j+1] = testlist[j+1], testlist[j] 
                swap = True

        if swap is False: 
            break

    print('Tested time: ', datetime.datetime.now() - start_time)

if __name__ == '__main__':
    bubblesort(createlist())
    