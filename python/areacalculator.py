# -*- coding: utf-8 -*-
"""areacalculator.py
a calculator that computes the 
area for either a circle or triangle """

print "Running area calculator..."

option = raw_input("Enter C for Circle or T for Triangle: ")

if option == 'C':
    radius = float(raw_input("Enter the radius of the circle: "))
    area = 3.14159 * radius**2
    print "Area: %f" % area
elif option == 'T':
    base = float(raw_input("Enter the base of the triangle: "))
    height = float(raw_input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print "Area: %f" % area
else:
    print "¡ERROR! Invalid shape."

print "Area calculator is closing..."