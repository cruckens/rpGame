import NPC

class Location(object):

    def __init__(self, name, level, type, exits = ''):
        self.name = name
        self.__level = level
        self.__description = 'No description'
        self.__exits = exits.split(',')
        self.__type = type
#        self.population = NPC.getPopulation(self.name)

    def __str__(self):
        if self.__type == 'City':
            return "%s - %s" % (self.name, self.__description)
        else:
            return "%s - %s\nDifficulty: %s" % (self.name, self.__description, self.__level)

    def setDescription(self, string):
        self.__description_ = string
        return self

    def getType(self):
        return self.__type

    def getExits(self):
        for i in self.__exits:
            return self.__exits

