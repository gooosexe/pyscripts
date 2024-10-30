from turtle import pd


def midpoint(x1, y1, x2, y2):
    return ((x1 + x2)/2, (y1 + y2)/2)

        
    

p1x = float(input("Point 1 x coordinate: "))
p1y = float(input("Point 1 y coordinate: "))

p2x = float(input("Point 2 x coordinate: "))
p2y = float(input("Point 2 y coordinate: "))

p3x = float(input("Point 3 x coordinate: "))
p3y = float(input("Point 3 y coordinate: "))

print(f'Point A: {p1x}, {p1y}')
print(f'Point B: {p2x}, {p2y}')
print(f'Point C: {p3x}, {p3y}')

pointA = (p1x, p1y)
pointB = (p2x, p2y)
pointC = (p3x, p3y)

# midpoints
pointD = midpoint(p1x, p1y, p2x, p2y)
pointE = midpoint(p2x, p2y, p3x, p3y)
pointF = midpoint(p3x, p3y, p1x, p1y)
print(f'midpoint of AB: {pointD}')
print(f'midpoint of BC: {pointE}')
print(f'midpoint of CA: {pointF}')

# medians
if pointE[0] <= pointA[0]:
    x2 = pointA[0]
    x1 = pointE[0]
    y2 = pointA[1]
    y1 = pointE[1]

    slope = (y2 - y1)/(x2- x1)
    yInt = y2 - x2 * slope
    print(f'y = {slope}x + {yInt}')

elif pointE[0] > pointA[0]:
    x2 = pointE[0]
    x1 = pointA[0]
    y2 = pointE[1]
    y1 = pointA[1]

    if x2 - x1 == 0:
        print(f'x = {x2}')
    else:
        slope = (y2 - y1)/(x2 - x1)
        yInt = y2 + (-x2) * (slope)
        print(f'y = {slope}x + {yInt}')

if pointF[0] <= pointB[0]:
    x2 = pointB[0]
    x1 = pointF[0]
    y2 = pointB[1]
    y1 = pointF[1]


    if x2 - x1 == 0:
        print(f'x = {x2}')
    else:
        slope = (y2 - y1)/(x2 - x1)
        yInt = y2 + (-x2) * (slope)
        print(f'y = {slope}x + {yInt}')

elif pointF[0] > pointB[0]:
    x2 = pointF[0]
    x1 = pointB[0]
    y2 = pointF[1]
    y1 = pointB[1]

    if x2 - x1 == 0:
        print(f'x = {x2}')
    else:
        slope = (y2 - y1)/(x2 - x1)
        yInt = y2 + (-x2) * (slope)
        print(f'y = {slope}x + {yInt}')


if pointD[0] <= pointC[0]:
    x2 = pointC[0]
    x1 = pointD[0]
    y2 = pointC[1]
    y1 = pointD[1]

    if x2 - x1 == 0:
        print(f'x = {x2}')
    else:
        slope = (y2 - y1)/(x2 - x1)
        yInt = y2 + (-x2) * (slope)
        print(f'y = {slope}x + {yInt}')

elif pointD[0] > pointC[0]:
    x2 = pointD[0]
    x1 = pointC[0]
    y2 = pointD[1]
    y1 = pointC[1]

    if x2 - x1 == 0:
        print(f'x = {x2}')
    else:
        slope = (y2 - y1)/(x2 - x1)
        yInt = y2 + (-x2) * (slope)
        print(f'y = {slope}x + {yInt}')

