from sys import stdin, stdout
import math

EPSILON = 1e-9 # quizas ya hay un paquete que la tenga

class Line:
    def __init__(self, x1, y1, x2, y2):
        # y = mx + b
        # m = slope
        # b = intercept
        self.slope = (y1 - y2) / (x1 - x2) if x1 != x2 else math.inf # pendiente (m), inf representa verticalidad
        self.intercept = y1 - (self.slope * x1) # ordenada al origen (b)

        if self.is_vertical():
            self.x = x1

    def is_vertical(self):
        return self.slope == math.inf

    def __eq__(self, value: object):
        # same slope and same y-intercept ; "misma" pendiente y "misma" ordenada
        return (abs(self.slope - value.slope) < EPSILON 
                and abs(self.intercept - value.intercept) < EPSILON)

    def parallel(self, other: "Line"):
        # same slope, different y-intercept ; "misma" pendiente, diferente ordenada
        return (abs(self.slope - other.slope) < EPSILON 
                and abs(self.intercept - other.intercept) >= EPSILON)

    def _vertical_intersect(self,other):
        """
        Other -> vertical line
        """
        y_intersect = (self.slope * other.x) + self.intercept

        return ("{:.2f}".format(other.x), "{:.2f}".format(y_intersect))

    def intersect(self, other: "Line"):
        intersect_point = None

        if self.parallel(other) or (self.is_vertical() and other.is_vertical() and self.x != other.x):
            # paralelas o ambas verticales con diferente x
            intersect_point = "NONE"
        
        elif self == other or (self.is_vertical() and other.is_vertical() and self.x == other.x):
            # iguales o ambas verticales con igual x
            intersect_point = "LINE"

        elif other.is_vertical():
            # solo una vertical
            intersect_point = self._vertical_intersect(other)

        elif self.is_vertical():
            # solo una vertical
            intersect_point = other._vertical_intersect(self) # same class can access private methods.

        elif not (self == other):
            # no son iguales y no cumplen nada de lo anterior
            x_intersect = (other.intercept - self.intercept) / (self.slope - other.slope)
            y_intersect = (self.slope * x_intersect) + self.intercept

            intersect_point = ("{:.2f}".format(x_intersect), "{:.2f}".format(y_intersect))

        return intersect_point


pairs = int(stdin.readline())

results = []

for _ in range(pairs):
    data_in = [int(data) for data in stdin.readline().strip().split(' ')]

    fst = Line(*data_in[:4]) # first line
    snd = Line(*data_in[4:]) # second line

    intersect = fst.intersect(snd)

    if type(intersect) is str:
        results.append(intersect)

    else:
        results.append("POINT {} {}".format(*intersect))


stdout.write('INTERSECTING LINES OUTPUT\n')
stdout.write('\n'.join(results) + '\n')
stdout.write('END OF OUTPUT\n')
