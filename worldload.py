import location
import gc

spawn = location.Location('Easy town', '0', 'City', 'Piggie plains')
newbie_loc = location.Location('Piggie plains', '0', 'Farm zone', 'Easy town')



def changeLoc(self, pos):
    if self.getExits().__contains__(pos):
       for i in gc.get_objects():
             if isinstance(i, location.Location) and i.name == pos:
                 print("You've travelled to ", i.name)
                 return i
    else:
        print("Wrong input. Stay home dude")
        return self
