import pygame
import time
import random

WIDTH = 840
HEIGHT = 840
FPS = 30

WHITE = (255, 255, 255)
GREEN = (0, 255, 0,)
BLUE = (0, 128, 254)
YELLOW = (255 ,255 ,0)
GRAY = (32,33,36)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(GRAY)
pygame.display.set_caption("Python Maze Generator")
clock = pygame.time.Clock()


x = 0                
y = 0                   
w = 20                   
grid = []
visited = []
stack = []
solution = {}


def build_grid(x, y, w):
    for i in range(1,41):
        x = 20                                                            
        y = y + 20                                                        
        for j in range(1, 41):
            pygame.draw.line(screen, WHITE, [x, y], [x + w, y])           
            pygame.draw.line(screen, WHITE, [x + w, y], [x + w, y + w])   
            pygame.draw.line(screen, WHITE, [x + w, y + w], [x, y + w])   
            pygame.draw.line(screen, WHITE, [x, y + w], [x, y])           
            grid.append((x,y))                                            
            x = x + 20                                                    


def push_up(x, y):
    pygame.draw.rect(screen, BLUE, (x + 1, y - w + 1, 19, 39), 0)        
    pygame.display.update()                                             


def push_down(x, y):
    pygame.draw.rect(screen, BLUE, (x +  1, y + 1, 19, 39), 0)
    pygame.display.update()


def push_left(x, y):
    pygame.draw.rect(screen, BLUE, (x - w +1, y +1, 39, 19), 0)
    pygame.display.update()


def push_right(x, y):
    pygame.draw.rect(screen, BLUE, (x +1, y +1, 39, 19), 0)
    pygame.display.update()


def single_cell( x, y):
    pygame.draw.rect(screen, GREEN, (x +1, y +1, 18, 18), 0)          
    pygame.display.update()


def backtracking_cell(x, y):
    pygame.draw.rect(screen, BLUE, (x +1, y +1, 18, 18), 0)        
    pygame.display.update()                                        


def solution_cell(x,y):
    pygame.draw.rect(screen, YELLOW, (x+8, y+8, 5, 5), 0)            
    pygame.display.update()                                       


def carve_out_maze(x,y):
    single_cell(x, y)                                              
    stack.append((x,y))                                            
    visited.append((x,y))                                          
    while len(stack) > 0:                                          
        time.sleep(.005)                                            
        cell = []                                                 
        if (x + w, y) not in visited and (x + w, y) in grid:      
            cell.append("right")                                  

        if (x - w, y) not in visited and (x - w, y) in grid:      
            cell.append("left")

        if (x , y + w) not in visited and (x , y + w) in grid:     
            cell.append("down")

        if (x, y - w) not in visited and (x , y - w) in grid:      
            cell.append("up")

        if len(cell) > 0:                                          
            cell_chosen = (random.choice(cell))                    

            if cell_chosen == "right":                             
                push_right(x, y)                                   
                solution[(x + w, y)] = x, y                        
                x = x + w                                         
                visited.append((x, y))                              
                stack.append((x, y))                          

            elif cell_chosen == "left":
                push_left(x, y)
                solution[(x - w, y)] = x, y
                x = x - w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "down":
                push_down(x, y)
                solution[(x , y + w)] = x, y
                y = y + w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "up":
                push_up(x, y)
                solution[(x , y - w)] = x, y
                y = y - w
                visited.append((x, y))
                stack.append((x, y))
        else:
            x, y = stack.pop()                           
            single_cell(x, y)                               
            time.sleep(.01)                                    
            backtracking_cell(x, y)                           


def plot_route_back(x,y):
    solution_cell(x, y)                                      
    while (x, y) != (20,20):                           
        x, y = solution[x, y]                            
        solution_cell(x, y)                                      
        time.sleep(.01)


x, y = 20, 20                     
build_grid(40, 0, 20)             
carve_out_maze(x,y)               
plot_route_back(800, 800)         

running = True
while running:

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False