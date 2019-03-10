def read(file):
    """ method to read file and return x,y coordinates"""
    fd = open(file,'r')

    # TODO: Read content of file and split by new line char (i.e "\n")

    # TODO: delete last element from array

    x_coords = []
    y_coords = []

    # loop over each line from array "content"
    for line in content:
        # TODO: split line by , to retreive X,Y coordinates and convert to float

        # TODO: append x to x_coords and y to y_coords

    return zip(x_coords,y_coords)    
        

coords = read("coords.txt")    
print('{:5} {:5}'.format("X", "Y"))
for x,y in coords:
    print('{:4.2f} {:4.2f}'.format(x,y)) 
