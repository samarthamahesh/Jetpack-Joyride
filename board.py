from base import DIMENSION

class Board:

    def __init__(self):
        self.__length = DIMENSION['length']
        self.__width = DIMENSION['width']
        self.__framewidth = DIMENSION['frame_width']
        self.__matrix = [[" " for i in range(DIMENSION['width'])] for j in range(DIMENSION['length'])]

    def printBoard(self, xdis):
        for i in range(0, self.__length):
            x = ''
            for j in range(xdis, xdis+self.__framewidth):
                x += self.__matrix[i][j]
            print(x)

    def get_matrix(self):
        return self.__matrix