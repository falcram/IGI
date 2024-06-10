class A:
    __c = "GRENN"
    color = "RED"
    def __init__(self):
        self.__width = 1123
    def __init__(self, width):
        self.__width = width
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width):
        if(width > 0):
            self.__width = width
        else:
            print("===MISTAKE=== IMPOSSIBLE WIDTH")
    def printColor(self):
        print(self.__c)
    def change_color(self, color_str):
        self.__c = color_str
            

a = A(999)


print(a.width)
a.width = -123
a.width = 12
print(a.width)