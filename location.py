class Location(object):

    def __init__(self, name, level, type, description, exits = ''):
        self.name = name
        self.__level = level
        self.__description = description
        self.__exits = exits.split(',')
        self.__type = type
        self.population = 0

    def __str__(self):
        if self.__type == 'City':
            return "%s - %s" % (self.name, self.__description)
        else:
            return "%s - %s\nDifficulty: %s" % (self.name, self.__description, self.__level)

    def setDescription(self, string):
        self.__description_ = string

    def getType(self):
        return self.__type

    def getExits(self):
            return self.__exits

    def showFeatues(self):
        if self.__type == 'City':
            a = input()
            #visit shops method call, any activity with npc etc
