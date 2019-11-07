def createlist():
    testlist = list()
    file = open("D:\\COLLEGE\\ACADEMIC\\III YEAR\\DAA_LAB\\TEST DATA\\descending.txt","r")
    count = 0
    for i in file:
        testlist.append(int(i))
        count += 1

        if count == 100:
            break
    file.close()
    return testlist

 
def partition(arr,low,high): 
    i = ( low-1 )        
    pivot = arr[high]     

    for j in range(low , high): 

        if arr[j] < pivot: 
        
            
            i = i+1
            arr[i],arr[j] = arr[j],arr[i] 

    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 


def quickSort(arr,low,high): 
    if low < high: 

        pi = partition(arr,low,high) 

        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

if __name__ == '__main__':
    import datetime
    arr = createlist()
    n = len(arr)

    start_time = datetime.datetime.now()
    quickSort(arr, 0, n-1)
    print('Tested time: ', datetime.datetime.now() - start_time)

    print(arr)
