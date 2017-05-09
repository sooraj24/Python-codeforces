
num1 = float(input("enter the 1st number"))

num2 = float(input("enter the 2st number"))

num3 = float(input("enter the 3st number"))

if (num1 > num2) and (num1 > num3):  
	largest = num1,

elif (num2 > num3) and (num2 > num1):
        largest = num2,

else:
        largest = num3,

print("the largest number among",num1,num2,num3,"is",largest)
