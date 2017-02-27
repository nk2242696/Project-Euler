import math
t=int(raw_input())
for xc in range(t):
        n=int(raw_input())
        num=math.sqrt(1+8*n)-1
        num=num/2
        if num-int(num)==0:
            print int(num)
        else:
            print "-1"
