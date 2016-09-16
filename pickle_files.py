import pickle

class FileManager():

    @staticmethod
    def filesave(data):
        with open('ids.pickle', 'wb') as f:
            pickle.dump(data, f)
        f.close()
        print ('Succesfully saved')

    @staticmethod
    def fileload(id):
        with open('ids.pickle', 'rb') as f:
            data = pickle.load(f)
            if data.id == id:
                f.close()
                return data
            else:
                return False
