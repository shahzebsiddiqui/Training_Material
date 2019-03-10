#1 
alpha = ['a','b','c','d']
print (alpha)
#2
x = [2,4] 
y = [8,10]
z = x+y
#3
z[0] = z[0]+2
z[1] = z[1]+2
z[2] = z[2]+2
z[3] = z[3]+2
print(z)
#4
print(z*2)
#5 
a=[x*2 for x in z]
print(a)
#6 
a = [1,4,9,16]
a = []
print (a)
#7 
print(len(a))
#8
a = [1,4,9,16]
a.append("a")
a.append(1.3)
a.append("hey")
print(a)
#9 
a = [x for x in range(10)]
print(a[::2])
