import math
 
                        # area of a square
side = float(input("What is the length of a side of the square?"))
area = side ** 2
print(f"the area of the square is : {area}")

print()
                         # area of a rectangle
length = float(input("What is the length of the rectangle?"))
width = float(input("What is the width of the rectangle"))
area = length * width
print(f"The area of the rectangle is: {area}")

print()
                        #area of a circle
radius = float(input("what is the radius of the Circle?"))
area = 3.14 *(radius ** 2)
print(f"the area of the Circle is:{area}")

print()
                   #using the math library
radius = float(input("What is the radius of the circle?"))
area = math.pi * (radius**2)
print(f"The area of the circle is: {area}")

print()
                  # many area from on value
value = float(input("What is the value to be used?"))
                  #calculate area
area_square = value ** 2
area_circle = math.pi * (value ** 2)
volume_cube = value ** 3
volume_sphere  = (4/3)* math.pi * ( value ** 3)
print(f"Area of the square:{ area_square}")
print(f"Area of a circle:{area_circle}")
print(f"Area of a cube: {volume_cube}")
print(f"Area of a sphere:{ volume_sphere}")
                      #Cm -> m conversion
       #area of a square                     
side = float(input("What is the length of the square ( in Cm)?"))
area = side ** 2
print(f"The area of the square is:{area} Cm^2")  
print(f"The area of the square is: {area/10000} m^2") 
      #Area of a rectangle
print()
length = float(input("What is the length of the rectangle (in Cm)?"))
width = float(input("What is the width of the rectangle (in Cm)?"))
area = length * width
print(f"The area of the rectangle is: {area} Cm^2")
print(f"The area of the rectangle is: {area/ 10000} m^2")
       # Area of a circle
print()
radius = float(input("What is the radius of the circle?"))
area = 3.14 * (radius ** 2)
print(f"The area of the circle is:{area}")
print(f"The area of the circle is:{area/10000} m^2 ")