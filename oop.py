import pickle_files

def login():
    id = input('Login: ').lower()
    user = pickle_files.fileload(id)
    if user == 'R':
        login()
    else:
        print('Manual menu\n1 - See info\n2 - See inventory\n3 - Farm some crips\n4 - Go anywhere\nS - Save progress\nL - Load account')
        return user

user = login()

while True:
    choice = input()
    if choice == '1':
        print(user.__str__())
    elif choice == '2':
        pass
    elif choice == '3':
        print(user.farm())
    elif choice == '4':
        print(user.getExits())
        user.setLocation(input('Type the name of the place you want to go: '))
    elif choice == 'S' or choice == 's':
        pickle_files.filesave(user)
        print('Succesfully saved')
    elif choice == 'l' or choice == "L":
        user = login()
    else:
        continue
