a=raw_input()
n1=n2=n3=0
for i in a:
    if i == '1':
        n1+=1
    elif i=='2':
        n2+=1
    elif i=='3':
        n3+=1
s = "1+" * n1 + "2+" * n2 + "3+" * n3
print s[:-1]
