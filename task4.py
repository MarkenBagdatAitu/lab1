import math

class Triangledim():
    def __init__(side, l1, l2, l3):
        side.l1 = l1
        side.l2 = l2
        side.l3 = l3
        side.p = side.l1+side.l2+side.l3
        side.s = side.p / 2.0

    def checktri(side):
        if (side.l1+side.l2>side.l3) and (side.l2+side.l3>side.l1) and (side.l1+side.l3>side.l2): 
            print("Perimeter of the triangle: %f" %side.p)
        else: 
            print("triangle didn't find") 

class TriArea(Triangledim):
    def findArea(side):
        area = math.sqrt(side.s*(side.s-side.l1)*(side.s-side.l2)*(side.s-side.l3))
        print("The area of the triangle: %f" %area)

if __name__ == "__main__":
    p = TriArea(int(input()), int(input()), int(input()))
    p.checktri()
    p.findArea()
