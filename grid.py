import pygame, random, sys


BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
SIZE = 4
BLOCK_SIZE = int(WINDOW_WIDTH / SIZE)
NODES = []


#NODE
#   X
#   Y
#   isNode
#   neighbors
#   

def main():
    global SCREEN, CLOCK
    #pygame.init()
    pygame.font.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)

    # Generate Nodes
    index = 0
    for row in range(0,SIZE):
        for col in range(0,SIZE):
            if random.random() > .1 or index == 0 or index == SIZE*SIZE:
                isNode = True #whitespot
            else:
                isNode = False #blackspot
            NODES.append({'x': col, 'y': row, 'isNode':isNode, 'neighbors':list()})
            index = index + 1


    for i in range(len(NODES)):
        if NODES[i]['x'] < SIZE-1:
            NODES[i]['neighbors'].append(i+1)
        if NODES[i]['y'] < SIZE-1:
            NODES[i]['neighbors'].append(i+SIZE)
        if NODES[i]['x'] > 0:
            NODES[i]['neighbors'].append(i-1)
        if NODES[i]['y'] > 0:
            NODES[i]['neighbors'].append(i-SIZE)
        print(NODES[i])
        


    slowloop=0
    #''' Happens every frame '''
    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        #if slowloop < len(NODES): 
            #NODES[slowloop]['isNode'] = False
        #slowloop = slowloop + 1
        #SCREEN.blit(pygame.font.render('Hello!', True, (255,0,0)), (200, 100))

        CLOCK.tick(5) #FrameRate
        pygame.display.update()

def drawGrid():
    for i in range(len(NODES)):
        rect = pygame.Rect(NODES[i]['x']*BLOCK_SIZE, NODES[i]['y']*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)

        if NODES[i]['isNode']:
            pygame.draw.rect(SCREEN, WHITE, rect, 0)
        else:
            pygame.draw.rect(SCREEN, BLACK, rect, 0)
        pygame.draw.rect(SCREEN, BLACK, rect, 1)

        info = str(i) + str(NODES[i]['neighbors'])
        my_font = pygame.font.SysFont('Arial', 10)
        text_surface = my_font.render(info, False, (0, 0, 0))
        SCREEN.blit(text_surface, (NODES[i]['x']*BLOCK_SIZE,NODES[i]['y']*BLOCK_SIZE))


main()