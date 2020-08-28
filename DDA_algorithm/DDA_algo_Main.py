from decimal import Decimal, ROUND_HALF_UP  # for proper number rounding operation
from DDA_algorithm.TableIt import TableIt  # table generation
import matplotlib.pyplot as plt  # graph


def dda(x1, y1, x2, y2):
    tbl = [["Steps", "x", "y"], [1, x1, y1]]  # list containing table data

    # x and y coordinates difference
    dx = x2 - x1
    dy = y2 - y1

    # magnitude
    m = dy / dx

    # m < 1
    if abs(dx) > abs(dy):
        steps = abs(dx)
        if x1 > x2:
            xinc = -1
            yinc = -m
        else:
            xinc = 1  # xinc = dx/steps
            yinc = m
    # m > 1
    else:
        steps = abs(dy)
        xinc = 1 / m
        yinc = 1  # yinc = dy/steps

    # Graph axis details
    plt.axis([0, x2 + 10, 0, y2 + 10])
    plt.scatter(x1, y1)  # mark the starting point on graph
    plt.scatter(x2, y2)  # mark the ending point on graph

    for i in range(steps):
        x1 += xinc
        y1 += yinc
        plt.scatter(x1, y1)
        plt.pause(0.5)
        tbl.append(
            [i + 2, Decimal(x1).quantize(0, ROUND_HALF_UP), Decimal(y1).quantize(0, ROUND_HALF_UP)])  # round up x and y

    # print the table
    TableIt.printTable(tbl, useFieldNames=True)
    plt.show()


x1, y1 = map(int, input('Enter coordinates for Staring point(x,y): ').strip().split(','))
x2, y2 = map(int, input('Enter coordinates for Ending point(x,y): ').strip().split(','))

dda(x1, y1, x2, y2)
