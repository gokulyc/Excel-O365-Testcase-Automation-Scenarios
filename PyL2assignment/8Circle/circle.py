from math import pi

class circle():

    def __init__(self,radius):
        self.radius=float(radius)

    def area(self):
        return pi*self.radius*self.radius
    
    def circumference(self):
        return 2*pi*self.radius

if __name__ == "__main__":
    radius=input('Enter radius :')

    cobj=circle(radius)

    print(f'For radius :{radius} Area:{cobj.area()} Circumference:{cobj.circumference()}')