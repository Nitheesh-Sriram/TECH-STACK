class parent:
    def __init__(self,name):
        self.name = name 
    

class child(parent):
    
    def show(self):
        print("Parent default constructor value = ",self.name)


c = child("69.69")
c.show()