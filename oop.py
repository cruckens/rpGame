import random
import Character
import pickle_files

id = input('Login: ')
user = pickle_files.FileManager.fileload(id)
if not user:
     user = Character.Character(id)
print('Manual menu\n1 - See info\n2 - See inventory\n3 - Farm some crips\n4 - Nope\nS - Save progress')
while True:
    choice = input()
    if choice == '1':
        print(user)
    elif choice == '2':
        pass
    elif choice == '3':
        print(user.farm())
    elif choice == '4':
        pass
    elif choice == 'S' or choice == 's':
        user.fileSave()
    else:
        continue
