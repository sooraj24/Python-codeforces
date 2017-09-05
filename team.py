n = int(raw_input())
count = 0
for i in range(0,n):
	b = raw_input()
	c = b.split()
	print c
	c = map(int, c)
	print c
	if(sum(c)>=2):
		count += 1
print count
