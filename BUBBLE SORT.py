import time


f = open("descending.txt","r")
li = []
for i in f:
    li.append(int(i))



start = time.time()
print(start)
i=0
for i in range(len(li)-1):
    j=0
    for j in range(len(li)-1-i):
        if li[j] > li[j+1]:
            temp = li[j+1]
            li[j+1] = li[j]
            li[j] = temp
            print("hek")


end = time.time()
print(end)
print(end - start)

