from decimal import Decimal, ROUND_HALF_UP  # for proper number rounding operation
from DDA_algorithm.TableIt import TableIt  # table generation
import matplotlib.pyplot as plt


def dda(x1, y1, x2, y2):
    tbl = [["x", "y"], [x1, y1]]  # list containing table data

    # x and y coordinates different
    dx = x2 - x1
    dy = y2 - y1

    # magnitude
    m = dy / dx

    if dx > dy:
        steps = dx
        xinc = 1  # xinc = dx/steps
        yinc = dy / steps
    else:
        steps = dy
        xinc = dx / steps
        yinc = 1  # yinc = dy/steps

    # Graph axis details
    plt.axis([0, x2 + 5, 0, y2 + 5])
    plt.scatter(x1, y1)     # mark starting point
    plt.scatter(x2, y2)     # mark ending point

    for i in range(steps):
        x1 += xinc
        y1 += yinc
        plt.scatter(x1, y1)
        plt.pause(0.5)
        tbl.append([Decimal(x1).quantize(0, ROUND_HALF_UP), Decimal(y1).quantize(0, ROUND_HALF_UP)])    # round up x and y

    # print the table
    TableIt.printTable(tbl, useFieldNames=True)
    plt.show()

dda(2, 3, 12, 8)
