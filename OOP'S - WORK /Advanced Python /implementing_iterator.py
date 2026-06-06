#problem statement : implement remote control class that allows you to press "next" button to go to next TV channel 
class remotecontrol():
    def __init__(self):
        self.channel = ["HBO","ESPN","ABC","CN"]
        self.index = -1

    def _iter_(self):
        return self 
    
    def _next_(self):
        self.index = self.index+1 
        if self.index == len(self.channel):
            raise StopIteration 
        return self.channel[self.index]
    
r = remotecontrol()
itr = iter(r)
print(next(itr))