#1
x = 2
if x == 2:
    print("True")
else:
    print("False")

#2
a=b=c=True
if a == True and b == True and c == True:
    print("True")
#3
b=False
if a ==  True or b == True:
    print("True")
#4
x="abcdef"
if len(x) < 4:
    print("short")
else:
    print("long")
#5
if len(x) < 4:
    print("short")
elif len(x) == 6:
    print("match")
else:
    print("long")
#6:
x=["hi","how","is","your","day?"]
for word in x:
    print(word,len(word))
#7
a = [x for x in range(10)]
for c in a:
    if c == 7:
        break;
    
    print(c)
#8
for c in a:
    if c % 2 == 0:
        print(c,"even")
    else:    
        print(c,"odd")
#9
print(list(range(5, 10)))
print(list(range(20, 40,2)))
print(list(range(-20, -60,-10)))
    
    
