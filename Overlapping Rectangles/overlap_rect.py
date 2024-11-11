import math
from sys import stdin, stdout

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def list_coords(self):
        return [
            self.x1,
            self.y1,
            self.x2,
            self.y2
        ]

    def overlapping_area(self, rect):
        # return overlapping rect or None
        x1 = max(self.x1, rect.x1)
        y1 = max(self.y1, rect.y1)
        x2 = min(self.x2, rect.x2)
        y2 = min(self.y2, rect.y2)

        res_rect = None

        if x1 < x2 and y1 < y2:
            res_rect = Rectangle(x1,y1,x2,y2)

        return res_rect

data_in = [data.strip() for data in stdin.readlines()]

casos = int(data_in.pop(0).strip())
end = False

res = []

while len(data_in):

    if data_in[0] == '': # empty line
        data_in.pop(0)
        continue

    # input
    rect1 = Rectangle(*[int(pos) for pos in data_in.pop(0).split(" ")])
    rect2 = Rectangle(*[int(pos) for pos in data_in.pop(0).split(" ")])

    overlapping = rect1.overlapping_area(rect2)

    if overlapping:
        res.append("{} {} {} {}".format(*overlapping.list_coords()))
    else:
        res.append("No Overlap")

stdout.write("\n\n".join(res) + '\n')