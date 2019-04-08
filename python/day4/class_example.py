import os
import sys
class country:
    city = []
    def __init__(self,name):
        self.name = name
    def add_city(self,*city):
        for i in city:
            self.city.append(i)
    def __repr__(self):
        #return(f"{self.name} {self.city}")
        return (f"{self.name}")

class File:
    def __init__(self,fname):
        self.name = fname
        self.ext = os.path.splitext(self.name)[1]
        self.fname  = os.path.splitext(self.name)[0]
        self.abspath = os.path.abspath(self.fname)
        self.x = 1
    def isFile(self):    
        if os.path.exists(self.abspath):
            return True
        else:
            return False
    def read(self):
        if not self.isFile():
            print(f"File {self.abspath} does not exist")
            sys.exit(0)
        fd = open(self.abspath,"r")
        content = fd.read()
        fd.close()
        return content

    def __str__(self):        
        return f"name: {self.name} filename: {self.fname} ext: {self.ext} abspath: {self.abspath}"    


usa = country("USA")
usa.add_city("Boston","Buffalo", "NYC")

spain = country("SPAIN")
spain.add_city("Barcelona","Madrid")

#print(usa.name,usa.city)
#print(spain.name, spain.city)
print(usa)
#print(spain)


bashrc = File(os.path.join(os.getenv("HOME"),".bashrc"))
etc_bashrc = File("/etc/bash.bashrc")
print(bashrc)
print(etc_bashrc)



content = bashrc.read()
print(content)


invalid_file = File("/xzy")
print(invalid_file)
invalid_file.read()
