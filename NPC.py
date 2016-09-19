class NPC():

    def __init__(self, name, lvl, ally, health, pos):
        self.name = name
        self.isAlly = bool(ally)
        self.health = health
        self.pos = pos
        self.level = lvl

    def __str__(self):
        return 'NPC: %s, %s lvl, %s HP' % (self.name, self.level, self.health)
