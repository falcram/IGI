from square import area as sq_area
from square import perimeter as sq_perimeter
from circle import area as ci_area
from circle import perimeter as ci_perimeter

a=int(input("Square side length: "))
r=int(input("Circle radius length: "))

print(f"Square area {sq_area(a)}")
print(f"Square perimeter {sq_perimeter(a)}")

print(f"Circle area {ci_area(a)}")
print(f"Circle perimeter {ci_perimeter(a)}")