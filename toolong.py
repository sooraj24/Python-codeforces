def toolong(w):
 if len(w) > 10:
   return w[0]+str(len(w) - 2)+w[-1]
 else:
   return w

m = input()
s = " "
for i in range (m):
  w = raw_input()
  s=s+"#"+toolong(w)
	
d=s.split("#")
for i in d:
  print i
