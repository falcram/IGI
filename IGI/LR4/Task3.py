import math
import matplotlib.pyplot as plt
import numpy as np

def Task3():    
    #list = [-1, -0.95, -0.9, -0.85, -0.8, -0.75, -0.7, -0.65, -0.6, -0.55, -0.5, -0.45, -0.4, -0.35, -0.3, -0.25, -0.2, -0.15, -0.1, -0.05, 0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1]

    class my_calculations:
        #list = [-1, -0.95, -0.9, -0.85, -0.8, -0.75, -0.7, -0.65, -0.6, -0.55, -0.5, -0.45, -0.4, -0.35, -0.3, -0.25, -0.2, -0.15, -0.1, -0.05, 0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1]
        def __init__(self):
            self.x_list = [-1, -0.95, -0.9, -0.85, -0.8, -0.75, -0.7, -0.65, -0.6, -0.55, -0.5, -0.45, -0.4, -0.35, -0.3, -0.25, -0.2, -0.15, -0.1, -0.05, 0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1]

        def additional_stat(slef, data):
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
            
        def my_arcsin(self,x, eps):
            """Calculate custom arcsin"""
            sum = x
            elem = x
            n=0
            while  abs(elem) > eps and n < 500:
                n+=1
                elem =  (math.factorial(2 * n) / ((2 ** (2 * n) * (math.factorial(n) ** 2))) * (x ** (2 * n + 1) / (2 * n + 1)))
                #print(elem)
                sum += elem  
            return sum, n
        def math_asin(self, x):
            res = []
            for i in x:
                res.append(math.asin(i))
            return res
        def make_y_list(self ,list):
            res_y = []
            res_n = []
            for i in list:
                res_y_par, res_n_par = self.my_arcsin(i, 0.0000000001)
                res_y.append(res_y_par)
                res_n.append(res_n_par)
            return res_y, res_n
        def main_calcualtions(self):
            #asinx = plt.subplots()
            #x = self.x_list
            x = np.linspace(-1, 1, 100)
            y,n = self.make_y_list(x)
            print(x[60]," | ",y[60])
            plt.plot(x,y, label='my asin', color = "red")
            plt.plot(x,self.math_asin(x), label = 'math asin', color = "blue")
            ax = plt.gca()
            ax.spines['left'].set_position('center')
            ax.spines['bottom'].set_position('center')
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            self.additional_stat(y)
            plt.title('График двух функций')
            plt.xlabel('x')
            plt.ylabel('y')
            plt.legend()
            plt.savefig("asin.png")
            plt.annotate(f"|{x[60]:.2f} | {n[60]} | {y[60]:.2f} | {math.asin(x[60]):.2f} | {0.0000000001}|", xy=(0.21212121212121215,0.2137450582106007),  xytext=(0.25, -0.5),arrowprops=dict(facecolor='black', shrink=0.05))
            plt.show()
            
            
    obj = my_calculations()
    obj.main_calcualtions()

#Task3()