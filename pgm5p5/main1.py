# main1.py
from graphics import rectangle, circle
from graphics.graphics_3d import cuboid, sphere

print("Rectangle:")
print("Area =", rectangle.area(10, 5))
print("Perimeter =", rectangle.perimeter(10, 5))

print("\nCircle:")
print("Area =", circle.area(7))
print("Perimeter =", circle.perimeter(7))

print("\nCuboid:")
print("Area =", cuboid.area(2, 3, 4))
print("Perimeter =", cuboid.perimeter(2, 3, 4))

print("\nSphere:")
print("Area =", sphere.area(5))
print("Perimeter =", sphere.perimeter(5))
