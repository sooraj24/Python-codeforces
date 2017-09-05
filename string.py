a=raw_input()
b=a.lower()
l=len(b)
v=['a','o','y','e','u','i']
result=""
for i in range (0,l):
    if b[i] not in v:
        result=result+'.'
        result=result+b[i]
print result
