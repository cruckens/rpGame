classes = ['Mage', 'Marksman', 'Warrior', 'Priest']
name = input('Welcome to the game. Set your name: ')
type = input('Set your class: \n1 - Mage\n2 - Marksman\n3 - Warrior\n4 - Priest\n')
n = 1
for keys in classes:
print (n, keys)
n += 1

user = character.Character(name, classes[n-1])
