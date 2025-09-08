import matplotlib.pyplot as plt
import os
import math

def koch_curve(p1, p2, depth):
    if depth == 0:
        return [p1, p2]
    else:
        x1, y1 = p1
        x2, y2 = p2

        dx = (x2 - x1) / 3
        dy = (y2 - y1) / 3

        pA = (x1 + dx, y1 + dy)
        pB = (x1 + 2*dx, y1 + 2*dy)

        angle = math.pi / 3
        px = pA[0] + math.cos(angle) * dx - math.sin(angle) * dy
        py = pA[1] + math.sin(angle) * dx + math.cos(angle) * dy
        pC = (px, py)

        return (koch_curve(p1, pA, depth - 1) +
                koch_curve(pA, pC, depth - 1)[1:] +
                koch_curve(pC, pB, depth - 1)[1:] +
                koch_curve(pB, p2, depth - 1)[1:])

def generate_snowflake(depth=3, half=False, filename="koch.png"):
    if half:
        points = koch_curve((0, 0), (1, 0), depth)
    else:
        p1 = (0.0, 0.0)
        p2 = (0.5, math.sqrt(3)/2)
        p3 = (1.0, 0.0)

        side1 = koch_curve(p1, p2, depth)
        side2 = koch_curve(p2, p3, depth)
        side3 = koch_curve(p3, p1, depth)

        points = side1 + side2[1:] + side3[1:]

    x, y = zip(*points)
    plt.figure(figsize=(6, 6))
    plt.axis('equal')
    plt.axis('off')
    plt.plot(x, y, color='blue')
    path = os.path.join("static", "images", filename)
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    return path
