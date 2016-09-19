import pickle
import character

def filesave(data):
    try:
        f = open(data.id + '.pickle', 'xb')
    except FileExistsError:
        f = open(data.id + '.pickle', 'wb')
    pickle.dump(data, f)
    f.close()

def fileload(id):
    try:
            f = open(id +'.pickle', 'rb')
            data = pickle.load(f)
            f.close()
            return data
    except FileNotFoundError:
        ch = input('No account. (R)etry or (C)reate new\n')
        if ch == 'R' or ch == 'r':
            return 'R'
        elif ch == 'C' or ch == 'c':
            data = character.Character(id)
            print('User created. Saving.')
            filesave(data)
            return data
        else:
            print('Wrong input')
            return 'R'
