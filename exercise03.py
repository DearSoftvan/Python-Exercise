#this is a program which accept the radius of a circle from user and compute the area.
#from math import pi //if you activate this line you shouldn't define the pi. You can use directly pi when you calculating anything.
def areaOfCircle(radius):
	pi=3.14
	return pi*radius*radius
	#we use radius**2 for the two to the power of radius.

#Test the function
r=float(input("Enter the radius of circle: "))
area=areaOfCircle(r)
print("The area of the circle is", area)
