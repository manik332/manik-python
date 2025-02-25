import math

def circle(radius):
    area=math.pi*radius**2
    peri=2*math.pi*radius
    return area,peri


radius=10
print(f"area and perimeter of circle is{circle(radius)}")