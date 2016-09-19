import random
import worldload


class Character():

    def __init__(self, id, lvl = 1):
        self.id = id
        self.gender = None
        self.__lvl = lvl
        self.__exp = 0
        self.__gold = 0
        self.__pos = worldload.spawn

    def __str__(self):
        if self.gender == None:
            a = input('Are you (m)ale of (f)emale?: ')
            if a == 'm' or a == 'M':
                self.gender = 'Male'
            elif a == 'f' or a == 'F':
                self.gender = 'Female'
            else:
                "Try again."
        return "Person: %s\nGender: %s\nLevel: %d\nGold: %d\nYou're at: %s" % (self.id, self.gender, self.__lvl, self.__gold, self.__pos)

    def getExits(self):
        return self.__pos.getExits()

    def setLocation(self, new):
        self.__pos = worldload.changeLoc(self.__pos,new)

    def farm(self):
        if self.__pos.getType() == 'Farm zone':
            exp = random.randint(3, 10)
            self.gotExp(exp)
            if 1 == random.randint(1,2):
                tmpgold = random.randint(10, 25)
                self.__gold += tmpgold
                return 'Have looted %d gold\nExperience earned: %d' % (exp, tmpgold)
            else:
                return 'Experience earned: %d' % (exp)
        else:
            return "You're not at the farm zone"

    def gotExp(self, exp):
        self.__exp += exp
        for i in range(100 * (self.__lvl + 1) * 0.5, 10000, 50* (self.__lvl + 1) * 0.5):
            print(i)
            if self.__exp >= i:
                self.__lvl += 1
                self.__exp -= i
                print('Lvlup!')
