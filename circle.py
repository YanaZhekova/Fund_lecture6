class Circle:
    pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        return self.pi * self.diameter

    def calculate_area(self):
        return self.pi * self.diameter/2*self.diameter/2

    def calculate_area_of_sector(self, angle):
        return (angle/360)*self.calculate_area()


circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
