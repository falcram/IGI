import numpy as np
from check_input import check_input
def Task5():
    class stat:
        def correl(self):
            print("Матрица корреляции:")
            print(np.corrcoef(np.array([1,2,3])))
    class execute(stat):
        def __init__(self, n_inp, m_inp):
            self.__n = None
            self.n = n_inp
            self.__m = None
            self.m = m_inp
            self.A = np.random.randint(low=0, high=1000, size=(self.__n,self.__m))
            print(self.A)
        @property
        def n(self):
            return self.__n
        @n.setter
        def n(self, inp):
            if type(inp) is int:
                if inp > 0:
                    self.__n = inp
                else:
                    print("Impossible matrix line size!")
            else:
                print("Not a number")
        @property
        def m(self):
            return self.__n
        @m.setter
        def m(self, inp):
            if type(inp) is int:
                if inp > 0:
                    self.__m = inp
                else:
                    print("Impossible matrix column size!")
            else:
                print("Not a number")
        def sort_l(self):
            sorted_A = self.A[self.A[:, -1].argsort()[::-1]]
            print("Отсортированная матрица:")
            print(sorted_A)
        def mean_of_last_column(self):
            mean_value = np.mean(self.A[:, -1])
            print(f"Среднее значение последнего столбца: {mean_value:.2f}")
        def mean_of_last_column_prog(self):
            sum_values = np.sum(self.A[:, -1])
            num_elements = self.A.shape[0]
            mean_value_manual = sum_values / num_elements
            print(f"Среднее значение (вручную): {mean_value_manual:.2f}")
        
        def numpy_bible(self):
            print("Array")
            arr = np.array([1, 2, 3])
            print(arr)
            print("Array square")
            arr = np.square(arr)
            print(arr)
            print("Array of 0")
            arr = np.zeros(3)
            print(arr)
            print("Array of 1")
            arr = np.ones(3)
            print(arr)
            print("Array from 0 to 100, 100 elements")
            arr = np.linspace(1, 100, 100)
            print(arr)
            print("Array from 1 to 4 elem")
            print(arr[1:4])
            self.correl()

        @staticmethod
        def additional_stat(self, data):
            average = np.mean(data)
            #print(f"Среднее арифметическое: {average:.2f}")
            print(f"Среднее арифметическое: {average:.2f}")
            median_value = np.median(data)
            print(f"Медиана: {median_value:.2f}")
            unique_values, counts = np.unique(data, return_counts=True)
            mode_value = unique_values[np.argmax(counts)]
            print(f"Мода: {mode_value:.2f}")
            variance = np.var(data)
            standard_deviation = np.std(data)
            print(f"Дисперсия: {variance:.2f}, СКО: {standard_deviation:.2f}")

        def main_f(self):
            self.sort_l()
            self.correl()
            self.mean_of_last_column()
            self.mean_of_last_column_prog()
            self.numpy_bible()
            #self.additional_stat()
    
    print("Input matrix line")
    line_s = check_input(int, "NO VALUE")
    print("Input matrix column")
    column_s = check_input(int, "NO VALUE")
    obj = execute(line_s,column_s)
    obj.main_f()
    execute.additional_stat(obj, obj.A)
#Task5()