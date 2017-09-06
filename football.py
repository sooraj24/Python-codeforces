a=raw_input()
count0=count1=0
flag=0
b=int(len(a))
for i in range (0,b):
    if (a[i]=='0'):
        count0=count0+1
        count1=0
    else:
        count1=count1+1
        count0=0
    if (count0==7 or count1==7):
        print "YES"
        flag=1
        break
if (flag == 0):
    print "NO"
