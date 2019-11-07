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


def mergeSort(arr):
    if len(arr) >1: 
        mid = len(arr)//2 
        L = arr[:mid] 
        R = arr[mid:]  

        mergeSort(L) 
        mergeSort(R) 

        i = j = k = 0
        
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
        

        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
        
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1


if __name__ == '__main__':
    import datetime
    arr = createlist()

    start_time = datetime.datetime.now()
    mergeSort(arr)
    print('Tested time: ', datetime.datetime.now() - start_time)