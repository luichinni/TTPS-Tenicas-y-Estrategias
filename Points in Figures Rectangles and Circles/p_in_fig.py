
import math
from sys import stdin, stdout

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def calculate_distance(self, pointB: "Point"):
        return math.sqrt(
            (pointB.x - self.x) * (pointB.x - self.x)
            + (pointB.y - self.y) * (pointB.y - self.y))

class Rectangle:
    
    def __init__(self, x1, y1, x2, y2):
        self.x1 = min(x1,x2)
        self.y1 = min(y1,y2)
        self.x2 = max(x2,x1)
        self.y2 = max(y2,y1)
        
    def contains_point(self, point: Point):
        return (
            point.x > self.x1 
            and point.x < self.x2
            and point.y < self.y2
            and point.y > self.y1
        )
        
class Circle:
    def __init__(self, x, y, r):
        self.center = Point(x,y)
        self.radius = r
        
    def contains_point(self, point: Point):
        return (
            point.calculate_distance(self.center) < self.radius
        )


# lectura de figuras
figures = []

for figure in stdin:
    fig_data = figure.strip().split(' ')
    
    if len(fig_data) == 1:
        break
    
    float_data = [float(data) for data in fig_data[1:]]
    
    if fig_data[0] == 'r':
        # 1 => x1, 2 => y1, 3 => x2, 4 => y2
        figures.append(Rectangle(*float_data))
    else: # fig_data[0] == 'c'
        # 1 => x, 2 => y, 3 => r
        figures.append(Circle(*float_data))
        

# procesamiento de puntos
output = []

for idp, points in enumerate(stdin):
    x, y = tuple([float(data) for data in points.strip().split(' ')])
    
    # fin de input
    if x == 9999.9 and y == 9999.9:
        break
    
    punto = Point(x,y)
    appeared = False
    
    for idf, figure in enumerate(figures):
        if figure.contains_point(punto):
            output.append("Point {} is contained in figure {}".format(idp+1,idf+1))
        
            if not appeared:
                appeared = True
    
    if not appeared:
        output.append("Point {} is not contained in any figure".format(idp+1))

stdout.write("\n".join(output) + "\n")