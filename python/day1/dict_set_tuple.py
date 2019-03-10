#1
country = {
    "USA": "New York",
    "Canada": "Toronto"
}
print (country)
#2
print(country["USA"])
#3
country["USA"] = "Boston"
print(country["USA"])
#4
dict = {x: x**2 for x in (2, 4, 6)}
for k,v in dict.items():
    print(k,v)
#5
for i, v in enumerate(['tic', 'tac', 'toe']):
    print i,v
#6
coord = (4,5,6,7,8)
print (coord[0])
#7
empty=()
print(len(empty))
#8 
vector = ((0,1),(2,3))
print(vector[0])
#9
for k,v in vector:
    k+=1
    v+=2
    print (k,v)
#10
state = {"CT","MA","CT"}
print(state)
#11
state.add("NY")
state.add("PA")
state.add("NJ")
print(state)
#12
europe = {"England", "France"}
asia = {"India", "China"}
print(europe.union(asia))
#13
print(set("abcd").intersection("ab"))
