def printtest():
    print("aaa ", end = " ")
    print("bb") 

def iterobj_metable():
    x = "abcde"
    x = ["a", "b","c","d","e"]
    #x[3] = "a"
    print(x[0::2])

def logiccheck():
    """Проверка логики"""
    print("текст2">"текст1")

def unicodfuncheck():
    print(ord("a"))

def list_try():
    arr = [1,2,3,4,5,6,7,8,9,10]
    print(arr.index(6))
def print_arr():
    i=-1
    res = ""
    while(i<=1):
        res += f"{round(i,3)}, "
        i+=0.05
    print(res)
print_arr()