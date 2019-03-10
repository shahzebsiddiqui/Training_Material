def read(file):
    fd = open(file,'r')
    content = fd.read().split("\n")
    del(content[-1])
    x_coords = []
    y_coords = []
    for line in content:
        x = float(line.split(",")[0])
        y = float(line.split(",")[1])
        x_coords.append(x)
        y_coords.append(y)

    return zip(x_coords,y_coords)    
        

coords = read("coords.txt")    
print('{:5} {:5}'.format("X", "Y"))
for x,y in coords:
    print('{:4.2f} {:4.2f}'.format(x,y)) 
