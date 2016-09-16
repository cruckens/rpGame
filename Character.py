import random
import pickle_files

class Character():

    def __init__(self, id, gender = None, lvl = 1, exp = 0, gold = 0):
        self.id = id
        self.gender = gender
        self.__lvl = lvl
        self.__exp = exp
        self.__gold = gold
    def __str__(self):
        return "Person: %s\nGender: %s\nLevel: %d\nGold: %d" % (self.id, self.gender, self.__lvl, self.__gold)

    def fileLoad(self, id):
        return pickle_files.FileManager.fileload(id)

    def farm(self):
        exp = random.randint(3, 10)
        self.gotExp(exp)
        if 1 == random.randint(1,2):
            tmpgold = random.randint(10, 25)
            self.__gold += tmpgold
            return 'Have looted %d gold\nExperience earned: %d' % (exp, tmpgold)
        else:
            return 'Experience earned: %d' % (exp)

    def gotExp(self, exp):
        self.__exp += exp
        for i in range(100, 10000, 50):
            if self.__exp >= i:
                self.__lvl += 1
                self.__exp -= i
                print('Lvlup!')

    def fileSave(self):
        pickle_files.FileManager.filesave(self)
