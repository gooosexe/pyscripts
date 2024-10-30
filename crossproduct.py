import math
point1str = []
point2str = []
crossProduct = [0,0,0]
print("Format: x y z (no commas)")

while (1):
    strp1 = input("Vector a: ")
    strp2 = input("Vector b: ")

    point1str = strp1.split(" ")
    point2str = strp2.split(" ")
    point1 = list(map(int, point1str))
    point2 = list(map(int, point2str))

    aMag = math.sqrt(point1[0]**2 + point1[1]**2 + point1[2]**2)
    bMag = math.sqrt(point2[0]**2 + point2[1]**2 + point2[2]**2)
    dotProduct = point1[0]*point2[0] + point1[1]*point2[1] + point1[2]*point2[2]

    if (aMag == 0 or bMag == 0): angle = 0
    else: angle = math.acos(dotProduct / (aMag * bMag))

    crossProduct[0] = (point1[1] * point2[2]) - (point1[2] * point2[1])
    crossProduct[1] = (point1[2] * point2[0]) - (point1[0] * point2[2])
    crossProduct[2] = (point1[0] * point2[1]) - (point1[1] * point2[0])

    finalmag = math.sqrt(crossProduct[0]**2 + crossProduct[1]**2 + crossProduct[2]**2)

    print(f"Vector a: ({point1[0]}, {point1[1]}, {point1[2]})")
    print(f"Vector b: ({point2[0]}, {point2[1]}, {point2[2]})")
    print(f"Vector a magnitude: {aMag}")
    print(f"Vector b magnitude: {bMag}")
    print(f"Dot product: {dotProduct}")
    print(f"Cross product: ({crossProduct[0]}, {crossProduct[1]}, {crossProduct[2]})")
    print(f"Cross product magnitude: {finalmag}")
    print(f"Angle: {angle}rad, {math.degrees(angle)}°")
    print("")