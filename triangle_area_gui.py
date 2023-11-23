'''
Author name: Jeremiah E. Ochepo
last Edited: 3/1/2020 (10PM)
Discription: Triangle Information GUI
'''
from graphics import*
import random
import math
active_flag = True


def main():
    print("Welcome to the Triangle Information GUI!")
    print("Click three points on the screen to create a triangle.")
    print("The program will then calculate the area of the triangle.")

    win = GraphWin('Shapes', 400, 400, autoflush=False)

    # Program Status Message
    msg = Text(Point(200.0, 20.0), 'Triangle Information')
    msg.setFace('helvetica')
    msg.setStyle('bold')
    msg.setSize(12)
    msg.draw(win)

    color_List = ['black', 'yellow', 'red', 'blue', 'white']

    # Get Points
    p1 = win.getMouse().draw(win)
    p2 = win.getMouse().draw(win)
    p3 = win.getMouse().draw(win)

    def shape_method():
        shape = Polygon(p1, p2, p3)
        shape.setFill(color_List[2])
        shape.setOutline(color_List[4])
        shape.draw(win)

    shape_method()

    # Get coordinate of p1
    p1_x = p1.getX()
    p1_y = p1.getY()

    # Get coordinate of p2
    p2_x = p2.getX()
    p2_y = p2.getY()

    # Get coordinate of p3
    p3_x = p3.getX()
    p3_y = p3.getY()

    # Side A
    def distnace_p1_to_p2():
        dx = p2_x - p1_x
        dy = p2_y - p1_y
        dx = dx**2
        dy = dy**2
        length = round(math.sqrt(dx + dy), 2)
        # print(f'Length of P1 to p2: {length}')
        return length

    distnace_p1_to_p2()

    # Side B
    def distnace_p2_to_p3():
        dx = p3_x - p2_x
        dy = p3_y - p2_y
        dx = dx**2
        dy = dy**2
        length = round(math.sqrt(dx + dy), 2)
        # print(f'Length of P2 to p3: {length}')
        return length

    distnace_p2_to_p3()

    # Side C
    def distnace_p3_to_p1():
        dx = p3_x - p1_x
        dy = p3_y - p1_y
        dx = dx**2
        dy = dy**2
        length = round(math.sqrt(dx + dy), 2)
        # print(f'Length of P3 to p1: {length}')
        return length

    distnace_p3_to_p1()

    # Calling function
    side_a = distnace_p1_to_p2()
    side_b = distnace_p2_to_p3()
    side_c = distnace_p3_to_p1()

    s = (side_a + side_a + side_a) / 2
    s = round(s, 2)

    def calculate_area():
        area = (s - side_a) * (s - side_b) * (s - side_c)
        area = (s * (area))
        area = math.sqrt(area)
        area = round(area, 2)
        print(f'Area of Triangle: {area}')

    calculate_area()

    msg.setText('Click any point to quit')
    pt = win.getMouse()
    win.close()


try:
    main()
except:
    pass
