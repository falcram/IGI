import csv

def Task1():
    class Product:
        name = str()
        price_old = float()
        price_new = float()
        def __init__(self, n, p_o, p_n):
            self.name = n
            self.price_old = p_o
            self.price_new = p_n
        def price_changes(self):
            if(self.price_old < self.price_new):
                #print(self.price_new*100/self.price_old -100)
                return self.price_new*100/self.price_old -100
            else:
                #print("False")
                return False
    
    class CSV_Operations:
        def Write(input_dict, FILENAME):
            with open(FILENAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(input_dict)
        def Read():
            return False
        
    my_dict = {"name":"Dmitro", "Old price":10,"New price":100}
    cl = Product(my_dict["name"],my_dict["Old price"], my_dict["New price"])
    print(cl.price_changes())

Task1()
