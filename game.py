import NPC
import character
import location

npc = NPC.NPC
dungeons = {
    'Karazhan': {
        'Morrowes': ['Staff of Wizardy',
                     'Helmcrusher\'s mace',
                     'Sword of might'],
        'Horsemen without head': ['Слюна собаки',
                                  "Член шмеля",
                                  "Глаз бедного котика"],
    },
    'Black Temple': {
        'Krevedka': ['Щупальце креведки',
                     "Обтягивающие лосины"],
        'Illidan': ['Barrier of Azzinoth',
                    'Edge of Azzinoth']
    },
    'Icecrown Citadel': {
        'Lord Marrowgar': ['Brinn\'throll',
                           'Frozen Needle',
                           'Обломок стены Ледяной Цитадели'],
        'Arthas, the Lich King': ["Королевский скипетр Теренаса II",
                                  'Митриос, наследие Бронзоборода',
                                  "Зов хаоса, топор королей Лордерона"]
    },
}

user = character.Character(input('Type your name\n'))
print('Manual menu\n1 - See info\n2 - See inventory\n3 - Farm some crips\n4 - Go to dungeon\nS - Save progress')
while True:
    choice = input()
    if choice == '1':
        print(user)
    elif choice == '2':
        print()
    elif choice == '3':
        print(user.farm())
    elif choice == '4':
        print()
    elif choice == 'S' or choice == 's':
        print(user.usersFileSave())
    elif choice == 'L' or choice == 'l':
        loc = location.Location('Spawn zone', 5)
    else:
        continue