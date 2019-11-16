def createlist():
    testlist = list()
    file = open("D:\\COLLEGE\\ACADEMIC\\III YEAR\\LAB\\DAA_LAB\\TEST DATA\\descending.txt","r")
    count = 0
    for i in file:
        testlist.append(int(i))
        count += 1

        if count == 100000:
            break
    file.close()
    return testlist


def radix_sort(alist, base=10):
    if alist == []:
        return
 
    def key_factory(digit, base):
        def key(alist, index):
            return ((alist[index]//(base**digit)) % base)
        return key
    largest = max(alist)
    exp = 0
    while base**exp <= largest:
        alist = counting_sort(alist, base - 1, key_factory(exp, base))
        exp = exp + 1
    return alist
 
def counting_sort(alist, largest, key):
    c = [0]*(largest + 1)
    for i in range(len(alist)):
        c[key(alist, i)] = c[key(alist, i)] + 1
 
    # Find the last index for each element
    c[0] = c[0] - 1 # to decrement each element for zero-based indexing
    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1]
 
    result = [None]*len(alist)
    for i in range(len(alist) - 1, -1, -1):
        result[c[key(alist, i)]] = alist[i]
        c[key(alist, i)] = c[key(alist, i)] - 1
 
    return result


if __name__ == '__main__':
    import datetime
    arr = createlist()
    k = max(arr)

    print("Array is: ", arr)

    start_time = datetime.datetime.now()
    result = radix_sort(arr)

    print("Sorted Array: ", result)
    print('Tested time: ', datetime.datetime.now() - start_time)