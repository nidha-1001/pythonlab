# main2.py
from graphics.rectangle import area, perimeter
from graphics.graphics_3d.sphere import area as sarea, perimeter as speri

print("Rectangle Area:", area(6, 4))
print("Rectangle Perimeter:", perimeter(6, 4))

print("Sphere Area:", sarea(5))
print("Sphere Perimeter:", speri(5))
