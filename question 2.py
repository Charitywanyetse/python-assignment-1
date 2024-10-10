#question 2
#Using a function,create a program that calculates the volume of a cylinder.
import math
radius = int(input("Enter the radius of the cylinder: "))
height = int(input("Enter the height of the cylinder: "))
pie = math.pi
volume = pie * radius**2 * height
print(volume)