class NPC(object):
    def __init__(self, name, level):
        self.name = name
        self.level = level
    def __str__(self):
        return 'NPC: %s, %s level' % (self.name, self.level)
    def isAlly(self):
        pass
    def location(self):
        pass
