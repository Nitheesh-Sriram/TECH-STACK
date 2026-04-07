class animal:
    def sound(self):
        print("Animal make sound")
    

class dog(animal):
    def sound(self):
        print("Dog Barks")
    

class cat(animal):
    def sound(self):
        print("Cat Meow")


d = dog()
c = cat()

d.sound()
c.sound()