def createlist():
    testlist = list()
    file = open("D:\\COLLEGE\\ACADEMIC\\III YEAR\\LAB\\DAA_LAB\\TEST DATA\\descending.txt","r")
    count = 0
    for i in file:
        testlist.append(int(i))
        count += 1

        if count == 10:
            break
    file.close()
    return testlist

 
def countSort(alist, largest):
    c = [0]*(largest + 1)
    for i in range(len(alist)):
        c[alist[i]] = c[alist[i]] + 1

    c[0] = c[0] - 1
    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1]
 
    result = [None]*len(alist)
 
    for x in reversed(alist):
        result[c[x]] = x
        c[x] = c[x] - 1
 
    return result
 
 

if __name__ == '__main__':
    import datetime
    arr = createlist()
    k = max(arr)

    print("Array is: ", arr)

    start_time = datetime.datetime.now()
    result = countSort(arr, k)

    print("Sorted Array: ", result)
    print('Tested time: ', datetime.datetime.now() - start_time) 

