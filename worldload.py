import location
import gc
import NPC

spawn = location.Location('Easy town', '0', 'City','A city with a thousand simple workers...', 'Piggie plains')
newbie_loc = location.Location('Piggie plains', '0', 'Farm zone', 'Farm as much as you can until we fix it', 'Easy town')
pig = NPC.NPC('Pig','1', False, 100, newbie_loc.name)
bpig = NPC.NPC('Big pig','2', False, 150, newbie_loc.name)
vbpig = NPC.NPC('Very big pig','3', False, 200, newbie_loc.name)

def changeLoc(current, pos):
    if current.getExits().__contains__(pos):
       for i in gc.get_objects():
             if isinstance(i, location.Location) and i.name == pos:
                 print("You've travelled to ", i.name)
                 showNPC(pos)
                 return i
    else:
        print("Wrong input. Stay home dude\n")
        return current

def showNPC(current):
    for i in gc.get_objects():
        if isinstance(i, NPC.NPC) and i.pos == current:
            print(i)
