# main3.py
from graphics.rectangle import *
from graphics.circle import *
from graphics.graphics_3d.cuboid import *
from graphics.graphics_3d.sphere import *

print("Rectangle Area:", area(8, 4))
print("Rectangle Perimeter:", perimeter(8, 4))

print("Circle Area:", area(7))
print("Circle Perimeter:", perimeter(7))

print("Cuboid Area:", area(2, 3, 4))
print("Cuboid Perimeter:", perimeter(2, 3, 4))

print("Sphere Area:", area(6))
print("Sphere Perimeter:", perimeter(6))
