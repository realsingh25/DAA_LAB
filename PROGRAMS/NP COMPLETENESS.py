import random
import matplotlib.pyplot as plt
from time import time

def KS(Pro,i,W):
    if i==0 or W==0:
        return 0
    elif Pro[0][i]>W:
        return KS(Pro,i-1,W)
    else:
        return max(KS(Pro,i-1,W),Pro[1][i]+KS(Pro,i-1,W-Pro[0][i]))

def main():
    n=1
    plt.xlabel('Input Size (N)')
    plt.ylabel('Execution Time (milli second)')
    values={}
    while(n<20):
        Pro=[[0],[0]]
        for i in range(1,n+1):
            Pro[0].append(random.randint(1,50))
            Pro[1].append(random.randint(1,100))
        t1 = time()
        KS(Pro,n,500)
        t2 = time()
        values[n] = (t2-t1)*1000
        n+=1

    plt.plot(list(values.keys()), list(values.values()))
    plt.savefig('KS.png')
    plt.show()


if __name__=='__main__':
    main()