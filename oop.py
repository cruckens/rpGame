import pickle_files

def login():
    id = input('Login: ').lower()
    user = pickle_files.fileload(id)
    if user == 'R':
        login()
    else:
        print('Manual menu\n1 - See info\n2 - See inventory\nG - Go anywhere\nS - Save progress\nL - Load account\nF - farm')
        return user

user = login()
trig = 1
while True:
    choice = input()
    if choice == '1':
        print(user.__str__())
    elif choice == '2':
        pass
    elif choice == 'G' or choice =='g':
        print(user.getExits())
        user.setLocation(input('Type the name of the place you want to go: '))
        trig = 2
    elif choice == 'S' or choice == 's':
        trig = -1
        pickle_files.filesave(user)
        print('Succesfully saved')
    elif choice == 'l' or choice == "L":
        if trig == 1:
            y = input('Are you want to save the progress?(y/n): ')
            if y == 'n':
                user = login()
                continue
            if y == 'y':
                pickle_files.filesave(user)
                user = login()
            else:
                trig = 1
        else:
            user = login()
    elif choice == 'F' or choice == 'f':
        print(user.farm())
    else:
        continue
