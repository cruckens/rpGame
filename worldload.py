import location

spawn = location.Location('Easy town', '0', 'City', 'Piggie plains,Lol u noob')
newbie_loc = location.Location('Piggie plains', '2', 'Farm zone', 'Easy town')


def changeLoc(self, pos):
    if self.getExits().__contains__(pos):
#        for i in gc.get_objects():
#            if i.name == pos:
#                print('You travelled for a bit and now you\'re in' + pos)
#                return i
