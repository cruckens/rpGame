text = 'Марина очень любит читать. Её любимый жанр это детектив. Ей нравятся запутанные истории. Желтое лицо это первый рассказ. Его написал Конан Дойль. Это её любимый писатель.'

l = text.split('. ')
avg, count = 0, 0 # avg для нахождения среднего значения, count что бы считать сколько предложений больше среднего значения
lst = [] # Сюда будем сохранять кол-ва слов в каждом предложении
for i in l: # Бежим по предложениям
    j = i.split(' ') # Делим предложения на слова
    lst.append(len(j)) # Считаем сколько слов в каждом предложении и сохраняем на потом
    avg += len(j) # Считаем общее кол-во слов во всём тексте
for i in lst: # В этом списке кол-во слов в каждом предложении
    if i > avg / len(l): # Тут сравниваем кол-во слов каждого предложения со средним
        count += 1  # Тут считаем сколько у нас накопилось предложений, где слов больше чем в среднем
print(count)



def usersFileSave(self):
    if not self.checkID(self.id):
        file = open(".txt", "a")
        data = str(self.id) + " " + self.gender + " " + str(self.__lvl) + " " + str(self.__exp) + " " + str(self.__gold)
        file.writelines(data + '\n')

        file.close()
        return 'Succesfully saved'
    else:
        pass
def checkID(self, id):
    file = open(".txt", "r")
    if file.read().__contains__(id):
        file.close()
        return True

def loadByID(self, id):
    file = open(".txt", "r")
    lst = file.read().rstrip()
    bottom = lst.find(id)
    for i in range(bottom,bottom + len(id)):
        self.id += lst[i]


