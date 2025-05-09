import math


class punkt3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance_to_origin(self):
        a = math.sqrt((self.x) ** 2 + (self.y) ** 2 + (self.z) ** 2)
        return a

    def add(self, other):
        if not isinstance(other, punkt3D):
            raise ValueError
        xnew = self.x + other.x
        ynew = self.y + other.y
        znew = self.z + other.z
        return punkt3D(xnew, ynew, znew)

    def __repr__(self):
        return f"x = {self.x}, y = {self.y}, z = {self.z}"






