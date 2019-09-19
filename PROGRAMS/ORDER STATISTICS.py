def createlist():
    testlist = list()
    file = open("C:\\Users\\cc2\\Desktop\\DAA_LAB\\TEST DATA\\random.txt","r")
    count = 0
    for i in file:
        testlist.append(int(i))
        count += 1

        if count == 1000:
            break
    file.close()
    return testlist

 
def kthSmallest(arr): 
    comparison = 1  
    length = len(arr) 
      

    if(length%2 == 0): 
        maximum = max(arr[0], arr[1])
        comparison+=1

        minimum = min(arr[0], arr[1]) 
        comparison+=1  
     
        i = 2
          
   
    else: 
        maximum = minimum = arr[0] 
        i = 1
          

    while(i < length - 1): 
        if arr[i] < arr[i + 1]:
            comparison+=1
            maximum = max(maximum, arr[i+1]) 
            comparison+=1    
            minimum = min(minimum, arr[i])
            comparison+=1
        else:
            comparison+=1
            maximum = max(maximum, arr[i]) 
            comparison+=1
            minimum = min(minimum, arr[i+1]) 
            comparison+=1
        i += 2
      
    return (maximum, minimum,comparison) 


if __name__ == '__main__':
    arr = createlist()
    maximum, minimum, comparison  = kthSmallest(arr)
    print("Minimum element is", minimum) 
    print("Maximum element is", maximum)
    print("Comparison is", comparison)
