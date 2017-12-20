class Traverse:
    __traversedata = ''
    __directions=['N','E','S','W']
    __Coordinate=[]
    __pos=''
    __position=''
    __dir=''

    def __init__(self,data={}):
        self.__data = data

    def get_Coordinates(self):
        self.__pos = self.__data[0]
        self.__position = (self.__pos.split(' '))
        self.__Coordinate.append(int(self.__position[0]))
        self.__Coordinate.append(int(self.__position[1]))
        self.__dir=self.__position[2]
        return  self.__Coordinate

    def get_TraverseString(self):
        self.__traversedata=self.__data[1]
        return self.__traversedata

    def L(self):
        if self.__Coordinate[0] <= 5 and self.__Coordinate[1] <= 5 and self.__dir in self.__directions:
            self.__dir = self.__directions[((self.__directions.index(self.__dir) - 1 + 4) % 4)]

    def R(self):
        if self.__Coordinate[0] <= 5 and self.__Coordinate[1] <= 5 and self.__dir in self.__directions:
            self.__dir = self.__directions[((self.__directions.index(self.__dir) + 1) % 4)]

    def M(self):

        if self.__dir == 'N' and self.__Coordinate[0] <= 5 and self.__Coordinate[1] <= 5: self.__Coordinate[1] += 1

        if self.__dir == 'W' and self.__Coordinate[0] <= 5 and self.__Coordinate[1] <= 5 : self.__Coordinate[0] -= 1

        if self.__dir == 'E' and self.__Coordinate[0] <= 5 and self.__Coordinate[1] <= 5 : self.__Coordinate[0] += 1

        if self.__dir == 'S' and self.__Coordinate[0] <= 5 and self.__Coordinate[1] <= 5 : self.__Coordinate[1] -= 1

    def printdata(self):
        return self.__Coordinate, self.__dir

    def toString(self):
        return 'Rover {}'.format(self.__Coordinate, self.__dir)