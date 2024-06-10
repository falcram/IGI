import abc
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from check_input import check_input
def Task4():
    class geom_figure(abc.ABC):
        @abc.abstractmethod
        def area():
            pass
    class figure_color():
        def __init__(self, col):
            self.__color = None 
            self.color = col
        @property
        def color(self):
            return self.__color
        @color.setter
        def color(self, inp):
            print(inp)
            print(type(inp))
            if type(inp) is str:
                self.__color = inp
            else:
                print("Not a color")
    class circle(geom_figure):
        def __init__(self, r, col):
            super().__init__()
            self.radius = r
            self.circle_color = figure_color(col)
        def area(self):
            return math.pi * self.radius**2
    class pentagon(geom_figure):
        name = ""
        def __init__(self, leng, col):
            super().__init__()
            self.__length = None
            self.length = leng
            self.pentagon_color = figure_color(col) 
        @property
        def length(self):
            return self.__length
        @length.setter
        def length(self, leng):
            if(type(leng) == int):
                if leng > 0:
                    self.__length = leng
                else:
                    print("Incorrect length!")
            else:
                print("Not a digit!")
        @property
        def color(self):
            return self.pentagon_color.color
        @color.setter
        def color(self, value):
            self.pentagon_color.color = value
        
        def area(self):
            b = self.length/(2*math.sin(math.pi/5))
            return 5*((self.length*math.sqrt(b**2 - self.length**2/4))/2) 
        
        def param(self):
            return "Side length: {} | Area: {} |Color: {}".format(self.length,self.area(),self.color)

        def Name(self):
            return self.name
        
        def draw(self):
            side_length = self.length

            # Вычисляем координаты вершин пятиугольника
            angles = np.linspace(0, 2 * np.pi, 6)[:-1]
            print(angles)
            x_coords = side_length * np.cos(angles)
            y_coords = side_length * np.sin(angles)
            print(x_coords)
            print(y_coords)
            print("Input Name:")
            name = check_input(str, "NO VALUE")
            # Создаем график
            plt.figure(figsize=(8, 8))
            plt.plot(x_coords, y_coords, marker='o', color=self.color, linestyle='', label = name)
            plt.fill(x_coords, y_coords, color=self.color, alpha=0.5)  # Закрашиваем пятиугольник

            plt.text(0, -self.length, name, fontsize=14)
            # Настраиваем оси и заголовок
            plt.axis('equal')
            plt.title('Pentagon')
            plt.savefig("Pentagon.png")
            plt.legend()
            # Отображаем график
            plt.show()

    print("Input Side Length:")
    pent_l = check_input(int, "NO VALUE")
    print("Input Color:")
    pent_c = check_input(str, "NO VALUE")
    #c = circle(10, 10)
    #p = pentagon(4, "red")
    p = pentagon(pent_l, pent_c)
    p.name = "ABCDE"
    p.draw()
#Task4()