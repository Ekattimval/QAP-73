class Rectangle:
    def _init_(self, a, b):
        self.a = a
        self.b = b
    def get_area(self):
        return self.a * self.b

class Square:
    def _init_(self, a):
        self.a = a
    def get_area_square(self):
        return self.a ** a

class Circle:
    def _init_(self, r):
        self.r = r
    def get_area_circle(self):
        return π * self.r **2
