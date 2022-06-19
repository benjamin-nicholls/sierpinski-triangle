import pygame
from math import sqrt
from random import uniform
from random import randint

def main() -> None:
    ITERATIONS = 10000
    TICK = 1000

    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 520
    DOT_RADIUS = 1
    BUFFER = 30
    
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    POINT_1 = (BUFFER, WINDOW_HEIGHT - BUFFER)
    POINT_2 = (WINDOW_WIDTH - BUFFER, WINDOW_HEIGHT - BUFFER)
    SIDE_LENGTH = (POINT_2[0] - POINT_1[0])
    POINT_3 = (BUFFER + (SIDE_LENGTH / 2), WINDOW_HEIGHT - BUFFER - sqrt(SIDE_LENGTH**2 - (SIDE_LENGTH/2)**2))
    points = [POINT_1, POINT_2, POINT_3]

    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Sierpinksi Triangle")

    # first random point
    while True:
        x = uniform(0, WINDOW_WIDTH)
        y = uniform(0, WINDOW_HEIGHT)
        if PointInTriangle(POINT_1, POINT_2, POINT_3, (x, y)):
            break
    lastPoint = (x, y)
    points.append(lastPoint)

    iterationCount = 0
    state = True
    while state:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = False
        iterationCount = iterationCount + 1
        
        if iterationCount < ITERATIONS:
            pygame.display.set_caption("Sierpinksi Triangle - iter: " + str(iterationCount))
            lastPoint = MidpointCoordinates(points[randint(0,2)], lastPoint)
            points.append(lastPoint)

        window.fill(WHITE)
        for p in points:
            pygame.draw.circle(window, BLACK, p, DOT_RADIUS)

        pygame.display.update()
        clock.tick(TICK)
        
    pygame.quit()
    return


def MidpointCoordinates(p1: tuple, p2: tuple) -> tuple:
    x = (p1[0] + p2[0]) / 2
    y = (p1[1] + p2[1]) / 2
    return (x, y)


def PointInTriangle(p1: tuple, p2: tuple, p3: tuple, p: tuple) -> bool:   
    ABC = AreaOfTriangleCoords(p1, p2, p3)
    PBC = AreaOfTriangleCoords(p, p2, p3)
    PAC = AreaOfTriangleCoords(p, p1, p3)
    PAB = AreaOfTriangleCoords(p, p1, p2)
    # Check if sum of PBC, PAC, PAB is same as ABC.
    return (ABC == PBC + PAC + PAB); 


def AreaOfTriangleCoords(p1: tuple, p2: tuple, p3: tuple) -> float:
    x1 = p1[0]
    x2 = p2[0]
    x3 = p3[0]
    y1 = p1[1]
    y2 = p2[1]
    y3 = p3[1]
    return abs((0.5)*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))


if __name__ == "__main__":
    main()