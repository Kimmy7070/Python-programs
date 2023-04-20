def area_circum(r):
    area=3.1416*r*r
    circum=2*3.1416*r
    return(area,circum)
r=int(input("Enter the radius"))
area,circum=area_circum(r)
print("The area of the circle is ",area)
print("The circumference of the circle is ",circum)