class Rover:
    __data = ''     #protected


    def __init__(self,data={}):
        self.__data = data

    def set_data(self,data):
        self.__data = data

    def get_data(self):
        return self.__data






