def cylinder(h,r):
    import math
    volume = math.pi * r**2 * h
    surface = 2*math.pi*r**2 + 2*math.pi*r*h
    print(f"The cylinder volume is {volume} and the surface area is {surface}.")

cylinder(5,2)
