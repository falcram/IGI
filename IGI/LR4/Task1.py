import csv
import pickle
from check_input import check_input
def Task1():
    class pickle_data:
        def serialize_pickle_class(class_obj):
            with open('data.pickle', 'wb') as f:
                pickle.dump(class_obj.convert_to_dict(), f)
        def serialize_pickle_dict(dict_obj):
            with open('data.pickle', 'wb') as f:
                pickle.dump(dict_obj, f)
        def deserialize_pickle():
            with open('data.pickle', 'rb') as f:
                return pickle.load(f)
    class PriceViewer(pickle_data):
        def __init__(self):
            self.products = []
            self.ser_dict = {}
        def add_poduct(self, class_obj):
            #self.products.clear()
            if_change = False
            for pr in self.products:
                if pr.name == class_obj.name:
                    pr.price_new = class_obj.price_new
                    if_change = True
                    break
            if if_change == False:
                self.products.append(class_obj)
        def del_product(self, class_obj):
            pass
        def calculate(self):
            for pr in self.products:
                if pr.price_changes() !=0:
                    print(f"Product: {pr.name} | Price changes: {pr.price_changes()}%")
        def serialize_pickle(self):
            for pr in self.products:
                pr.add_to_dict(self.ser_dict)
            with open('data.pickle', 'wb') as f:
                pickle.dump(self.ser_dict, f)
        def deserialize_pickle(self):
            with open('data.pickle', 'rb') as f:
                self.ser_dict = pickle.load(f)
                print(self.ser_dict)
            for key, value in self.ser_dict.items():
                self.add_poduct(Product(key, value[0], value[1]))
        def serialize_csv(self):
            for pr in self.products:
                pr.add_to_dict(self.ser_dict)
            with open('mycsvfile.csv', 'w') as f:  # You will need 'wb' mode in Python 2.x
                w = csv.DictWriter(f, self.ser_dict.keys())
                w.writeheader()
                w.writerow(self.ser_dict)
        def deserialize_csv(self):
            with open('mycsvfile.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.ser_dict=row
            for key, value in self.ser_dict.items():
                values = value.strip("()").split(", ")
                float_list = [float(value) for value in values]
                self.add_poduct(Product(key, float_list[0], float_list[1]))
        def show_poducts(self):
            for pr in self.products:
                pr.print_stat()
        def find_product(self, f_str):
            for pr in self.products:
                if pr.name == f_str :
                    pr.print_stat()
        def create_product(self):
            while(True):
                print("Input name")
                name = check_input(str, "NO VALUE")
                price = check_input(float, "NO VALUE")
                self.add_poduct(Product(name, price, price))
                print("Do you want create more products:\n1)Yes\n2)No")
                ans = input()
                if(ans == '2'):
                    break
                elif(ans == '1'):
                    continue
                else:
                    print("Incorrect input")
                    break

            
    class Product:
        def __init__(self, n, p_o, p_n):
            self.name = n
            if (type(p_o) is not float or type(p_n) is not float):
               raise Exception("ERROR: Incorrect TYPE!")
            if(p_o < 0 and p_n < 0):
                raise Exception("ERROR: Incorrect value!") 
            self.__price_old = p_o
            self.__price_new = p_n
        def __eq__(self, ch_inp):
            return self.name == ch_inp.name
        def print_stat(self):
            print(f"Product: {self.name} | Old price: {self.__price_old} | New price {self.__price_new}")
        @property
        def price_old(self):
            return self.__price_old
        @property
        def price_new(self):
            return self.__price_new
        @price_new.setter
        def price_new(self, inp):
            if (type(inp) is not float):
                raise Exception("ERROR: Incorrect TYPE!")
            if(inp < 0):
                raise Exception("ERROR: Incorrect value!")
            if(self.__price_new != inp ):
                self.__price_old = self.__price_new
                self.__price_new = inp 
        def convert_to_dict(self):
            return {self.name:[self.__price_old,self.__price_new]}
        def add_to_dict(self, inp_dict):
            inp_dict[self.name] = self.__price_old,self.__price_new
            return inp_dict 
        def price_changes(self):
            return self.price_new*100/self.price_old -100

    
    class CSV_Operations:
        def Write(input_dict, FILENAME):
            with open(FILENAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(input_dict)
        def Read():
            return False
        
    
    

    shop = PriceViewer()
    #shop.create_product()
    
    a = Product("ApplePhone", 4000.0, 4001.0)
    a.price_new = 8.0
    a1 = Product("Samsung A50", 600.0, 400.0)
    shop.add_poduct(a)
    shop.add_poduct(a1)
    shop.serialize_csv()
    #shop.deserialize_pickle()
    #shop.deserialize_csv()
    #shop.find_product()
   # shop.serialize_pickle()
    #shop.calculate()
    
    #shop.show_poducts()
    name = input()
    shop.find_product(name)
    #shop.find_product("Samsung A50")
    #mydict = {}
    #a.add_to_dict(mydict)
    #a1.add_to_dict(mydict)
    #serialize_pickle_dict(mydict)
    #b = deserialize_pickle()
    #print(b)
    #my_dict = {"name":"Dmitro", "Old price":10,"New price":100}
    #cl = Product(my_dict["name"],my_dict["Old price"], my_dict["New price"])
    #print(cl.price_changes())

#Task1()
