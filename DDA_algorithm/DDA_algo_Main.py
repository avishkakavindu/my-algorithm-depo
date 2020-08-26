from decimal import Decimal, ROUND_HALF_UP  # for proper number rounding operation
from DDA_algorithm.TableIt import TableIt   # table generation
import matplotlib.pyplot as plt


def dda(x1, y1, x2, y2):

    tbl = [["x", "y"], [x1, y1]] # list containing table data

    # x and y coordinates different
    dx = x2 - x1
    dy = y2 - y1

    # magnitude
    m = dy/dx

    if dx > dy:
        steps = dx
        xinc = 1    # xinc = dx/steps
        yinc = dy/steps
    else:
        steps = dy
        xinc = dx/steps
        yinc = 1    # yinc = dy/steps

    # Graph axis details
    plt.axis([x1-5, x2+5, y1-5, y2+5])
    plt.scatter(x1, y1, label="start")
    plt.scatter(x2, y2)

    for i in range(steps):
        x1 += xinc
        y1 += yinc
        plt.scatter(x1, y1)
        plt.pause(0.5)
        tbl.append([Decimal(x1).quantize(0, ROUND_HALF_UP), Decimal(y1).quantize(0, ROUND_HALF_UP)])
    TableIt.printTable(tbl, useFieldNames=True)
    plt.show()

dda(2,3,12,8)


# plt.axis([0, 10, 0, 1])
#
# for i in range(10):
#     y = np.random.random()
#     plt.scatter(i, y)
#     plt.pause(0.05)
#
# plt.show()