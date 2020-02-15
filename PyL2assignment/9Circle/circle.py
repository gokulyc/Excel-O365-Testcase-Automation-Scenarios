from math import pi

class circle():

    def __init__(self):
        self.radius=float(10)

    def area(self):
        return pi*self.radius*self.radius
    
    def circumference(self):
        return 2*pi*self.radius

if __name__ == "__main__":
    cobj=circle()

    print(f'For radius :{cobj.radius} Area:{cobj.area()} Circumference:{cobj.circumference()}')