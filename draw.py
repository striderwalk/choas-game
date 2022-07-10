import contextlib
with contextlib.redirect_stdout(None):
    import pygame
import os, glob

class Draw:


    pygame.init()
    clock = pygame.time.Clock()
    @classmethod
    def done(cls):
        pygame.quit()

    @classmethod
    def draw(cls, point_list : list, WIDTH= 750, HEIGHT = 550, xoff=True, yoff=True, HOLD=True, wait=0) -> None:

        # get win
        if not hasattr(cls, "win"):
            xboarder, yboarder = 50, 50
            cls.win = pygame.display.set_mode((WIDTH, HEIGHT))
            cls.xoff = (WIDTH) /2 * xoff
            cls. yoff = (HEIGHT) /2 * yoff
            

        # draw
        cls.win.fill((255,255,255))
        pygame.draw.lines(cls.win, (0,0,0), False, cls.__centerPoints(point_list,cls.xoff,cls.yoff))
        pygame.display.update()
        cls.clock.tick(wait) 

        # check for quit
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  exit()

        while HOLD:
            cls.clock.tick(5) 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  exit()
    @classmethod
    def draw_lines(cls, line_list : list, WIDTH= 750, HEIGHT = 550, xoff=True, yoff=True, HOLD=True, wait=0) -> None:

        # get win
        if not hasattr(cls, "win"):
            xboarder, yboarder = 50, 50
            cls.win = pygame.display.set_mode((WIDTH, HEIGHT))
            cls.xoff = (WIDTH) /2 * xoff
            cls. yoff = (HEIGHT) /2 * yoff


        cls.win.fill((255,255,255))
        for line in line_list:
            if line == []: continue

            pygame.draw.lines(cls.win, (0,0,0), False, cls.__centerPoints(line,cls.xoff,cls.yoff))
        
        pygame.display.update()
        cls.clock.tick(wait)

        # check for quit
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  exit()

        while HOLD:
            cls.clock.tick(5) 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  exit()
    @classmethod
    def dots(cls, dots : list, WIDTH= 750, HEIGHT = 550, xoff=True, yoff=True, HOLD=True, wait=0) -> None:


         
        # get win
        if not hasattr(cls, "win"):
            xboarder, yboarder = 50, 50
            cls.win = pygame.display.set_mode((WIDTH, HEIGHT))
            cls.xoff = (WIDTH) /2 * xoff
            cls.yoff = (HEIGHT) /2 * yoff


        cls.win.fill((255,255,255))



        cls.win.fill((255,255,255))
        for dot in dots:
            # print(dot)
            pygame.draw.circle(cls.win, (0,0,0), dot+(cls.xoff,cls.yoff), 1)
            # pygame.display.update() 
 
        pygame.display.update()
        cls.clock.tick(wait)

        # check for quit
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  exit()

        while HOLD:
            cls.clock.tick(5) 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  exit()

    @staticmethod
    def __centerPoints(points : list, xoff = 0, yoff = 0) -> list:
        # return centered points
        try:
            return [i + (xoff, yoff) for i in points]
        except Exception as e:
            print(points)
            raise e



    @staticmethod
    def __hex_to_rgb(hex: str) -> tuple:
        rgb = []
        for i in range(1,6,2):
            decimal = int(hex[i:i+2], 16)
            rgb.append(decimal)
        return tuple(rgb)


   