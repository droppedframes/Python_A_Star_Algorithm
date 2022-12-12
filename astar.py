from os import close
import pygame, random, sys, math



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0,255,0)

WINDOW_HEIGHT = 700
WINDOW_WIDTH = 700
SIZE = 20
BLOCK_SIZE = int(WINDOW_WIDTH / SIZE)
NODES = []
START = 40
END = 79 #SIZE*SIZE-1
OPEN_SET = []
CLOSED_SET = []
CURRENT = START
FOUND_PATH = 0
PATH = []

#NODE
#   X
#   Y
#   isNode
#   neighbors
#   f
#   g
#   h
#   prevous

def main():
    global SCREEN, CLOCK
    global FOUND_PATH
    global NODES
    global CURRENT
    global END
    #pygame.init()
    pygame.font.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)

    # Generate Nodes
    index = 0
    for row in range(0,SIZE):
        for col in range(0,SIZE):
            if random.random() > 0.25 or index == START or index == END:
                isNode = True #whitespot
            else:
                isNode = False #blackspot
            NODES.append({'x': col, 'y': row, 'isNode':isNode, 'neighbors':list(), 'f':0, 'g':0, 'h':0,'previous':None})
            index = index + 1


    for i in range(len(NODES)):
        if NODES[i]['x'] < SIZE-1 and NODES[i+1]['isNode'] == True: #3:00
            NODES[i]['neighbors'].append(i+1)
        if NODES[i]['y'] < SIZE-1 and NODES[i+SIZE]['isNode'] == True: #6:00
            NODES[i]['neighbors'].append(i+SIZE)
        if NODES[i]['x'] > 0 and NODES[i-1]['isNode'] == True:      #12:00
            NODES[i]['neighbors'].append(i-1)
        if NODES[i]['y'] > 0 and NODES[i-SIZE]['isNode'] == True:      #9PM
            NODES[i]['neighbors'].append(i-SIZE)


        ''' add diagnal neighbors
        if NODES[i]['x'] > 0 and NODES[i]['y'] > 0 and NODES[i-1-SIZE]['isNode'] == True:#10:30
            NODES[i]['neighbors'].append(i-1-SIZE)
        if NODES[i]['x'] < SIZE-1 and NODES[i]['y'] > 0 and NODES[i+1-SIZE]['isNode'] == True:#1:30
            NODES[i]['neighbors'].append(i+1-SIZE)      
        if NODES[i]['x'] < SIZE-1 and NODES[i]['y'] < SIZE-1 and NODES[i+1+SIZE]['isNode'] == True: #4:30
            NODES[i]['neighbors'].append(i+1+SIZE)      
        if NODES[i]['x'] > 0 and NODES[i]['y'] < SIZE-1 and NODES[i-1+SIZE]['isNode'] == True: #7:30
            NODES[i]['neighbors'].append(i-1+SIZE)
        # '''
    #print(NODES[i])
    OPEN_SET.append(START)
    

    slowloop=0

    #''' Happens every frame '''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if (len(OPEN_SET)> 0):
            winner = 0
            for i in range(len(OPEN_SET)):
                if NODES[OPEN_SET[i]]['f'] < NODES[OPEN_SET[winner]]['f']:
                    winner = i

            #current = the nodeID in openSet having the lowest fScore value
            CURRENT = OPEN_SET[winner]
            lastCheckedNode = CURRENT

            tempN = CURRENT
            
            while NODES[tempN]['previous'] is not None:
                PATH.append(NODES[tempN]['previous'])
                tempN = NODES[tempN]['previous']

            #Did I finish?
            if CURRENT == END:
                FOUND_PATH = 1
                print('DONE!')
                continue
            
            #Best option moves from openSet to closedSet
            OPEN_SET.remove(CURRENT)
            CLOSED_SET.append(CURRENT)

            # Check all the neighbors
            neighbors = NODES[CURRENT]['neighbors']

            #print('Searching seighbors:')
            for i in range(len(neighbors)):
                neighbor = neighbors[i]
                
                #Valid next spot?
                if neighbor not in CLOSED_SET:
                    # Is this a better path than before?
                    tempG = NODES[CURRENT]['g'] + getHeuristic(CURRENT,neighbor)

                    if neighbor not in OPEN_SET:
                        OPEN_SET.append(neighbor)
                        NODES[neighbor]['g'] = tempG
                        NODES[neighbor]['h'] = getHeuristic(neighbor,END)
                        NODES[neighbor]['f'] = NODES[neighbor]['g'] + NODES[neighbor]['h']
                        NODES[neighbor]['previous'] = CURRENT
                    elif tempG < NODES[neighbor]['g']:
                        NODES[neighbor]['g'] = tempG
                        NODES[neighbor]['h'] = getHeuristic(neighbor,END)
                        NODES[neighbor]['f'] = NODES[neighbor]['g'] + NODES[neighbor]['h']
                        NODES[neighbor]['previous'] = CURRENT


        else:
            print("NO Solution!!")
            continue



        #if slowloop < len(NODES): 
            #NODES[slowloop]['isNode'] = False
        #slowloop = slowloop + 1
        #SCREEN.blit(pygame.font.render('Hello!', True, (255,0,0)), (200, 100))

        CLOCK.tick(20) #FrameRate
        drawGrid()
        pygame.display.update()
        PATH.clear()

def drawGrid():
    global FOUND_PATH
    global NODES
    global PATH
    global CURRENT

    for i in range(len(NODES)):
        rect = pygame.Rect(NODES[i]['x']*BLOCK_SIZE, NODES[i]['y']*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)

        if i == END:
            pygame.draw.rect(SCREEN, (0,0,255), rect, 0)
        elif i in PATH:
            pygame.draw.rect(SCREEN, (255,0,0), rect, 0)
        elif i in OPEN_SET:
            pygame.draw.rect(SCREEN, (0,130,0), rect, 0)
        elif i in CLOSED_SET:
            pygame.draw.rect(SCREEN, GREEN, rect, 0)
        elif NODES[i]['isNode']:
            pygame.draw.rect(SCREEN, WHITE, rect, 0)
        else:
            pygame.draw.rect(SCREEN, BLACK, rect, 0)

        pygame.draw.rect(SCREEN, BLACK, rect, 1)

        #info = str(i) + str(NODES[i]['neighbors'])
        info = str(NODES[i]['g'])
        #info = str(NODES[i]['f'])
        my_font = pygame.font.SysFont('Arial', 10)
        text_surface = my_font.render(info, False, (0, 0, 0))
        SCREEN.blit(text_surface, (NODES[i]['x']*BLOCK_SIZE,NODES[i]['y']*BLOCK_SIZE))

        text_surface2 = my_font.render(str(NODES[i]['h']), False, (0, 0, 0))
        SCREEN.blit(text_surface2, (NODES[i]['x']*BLOCK_SIZE,NODES[i]['y']*BLOCK_SIZE+12))
        

def getHeuristic(a,b):
    distance = 0.0
    Ax=NODES[a]['x']
    Ay=NODES[a]['y']
    Bx=NODES[b]['x']
    By=NODES[b]['y']
    distance = math.dist([Ax, Ay], [Bx, By])
    #distance = abs(NODES[a]['x'] - NODES[b]['x']) + abs(NODES[a]['y']- NODES[b]['y'])
    return distance


print('start')
main()