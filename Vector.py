#Vector
from math import sin, cos, atan, hypot

# The quick way to know how big the pie is
PI = 3.141592653589793238462643383
TwoPI = PI * 2.0
HalfPI = PI * 0.5
OneAndHalfPI = PI * 1.5

# new math function
def direction(x, y):
    """Return the direction component of a vector (in radians), given
    cartesian coordinates.
    """
    if x > 0:
        if y >= 0:
            return atan(y / x)
        else:
            return atan(y / x) + TwoPI
    elif x == 0:
        if y > 0:
            return HalfPI
        elif y == 0:
            return 0
        else:
            return OneAndHalfPI
    else:
        return atan(y / x) + PI


class Vector:
    """Store a vector in cartesian coordinates."""


    def __init__(self,x,y):
        f = 0.0
        mag = 0.0
        self.x = x
        self.y = y

    def add(self, b):
        """Add b to self, where b is another Vector."""
        self.x += b.x
        self.y += b.y

    def heading(self):
        """Return the direction of the Vector in radians."""
        return direction(self.x, self.y)

    def mag(self):
        """Return the magnitude of the Vector."""
        return hypot(self.x, self.y)
