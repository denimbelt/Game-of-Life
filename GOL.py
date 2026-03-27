import pygame
import sys
import random 

pygame.init()

NEIGHBOUR_OFFSETS = [(-1,-1),(1,1),(-1,1),(1,-1),(0,1),(1,0),(0,-1),(-1,0)]
existing_cells = {}
previous_gen = []
current_gen = []
requests = {}
cell_size = 10

pygame.display.set_caption('Game of Life')
size = (500,500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

#calculates existing cells
for x in range(0,size[0]//cell_size):
    for y in range(0,size[1]//cell_size):
        existing_cells[str(x) + ';' +str(y)] = pygame.Rect(x*cell_size,y*cell_size,cell_size,cell_size)


#activates cells closer to 0,0
for i in range(size[0]*size[1]//cell_size):
        x = random.randint(0,size[0]//cell_size-1)%random.randint(1,size[0]//cell_size)
        y = random.randint(0,size[1]//cell_size-1)%random.randint(1,size[1]//cell_size)
        requests[str(x) + ';' + str(y)] = {'requests':3, 'pos':(x,y)}

while True:
    screen.fill((0,0,0))

    
    #filters cells to create next generation
    for pos in requests:
        if not (requests[pos]['requests'] <= 1 or requests[pos]['requests'] >= 4):

            if (requests[pos]['pos'] in previous_gen and (requests[pos]['requests'] == 2 or requests[pos]['requests'] == 3)):
                current_gen.append(requests[pos]['pos'])

            elif (requests[pos]['pos'] not in previous_gen and requests[pos]['requests'] == 3):
                current_gen.append(requests[pos]['pos'])

    requests.clear()

    for c in current_gen:

        pygame.draw.rect(screen,(255,255,255),existing_cells[str(c[0]) + ';' +str(c[1])])

        #creates requests for neighbours
        for n in NEIGHBOUR_OFFSETS:
            if str(c[0]+n[0]) + ';' +str(c[1]+n[1]) in existing_cells:

                if str(c[0]+n[0]) + ';' +str(c[1]+n[1]) not in requests:
                    requests[str(c[0]+n[0]) + ';' +str(c[1]+n[1])] = {'requests':0, 'pos':(c[0]+n[0],c[1]+n[1])}
                    requests[str(c[0]+n[0]) + ';' +str(c[1]+n[1])]['requests'] += 1

                else:
                    requests[str(c[0]+n[0]) + ';' +str(c[1]+n[1])]['requests'] += 1

    previous_gen = current_gen
    current_gen = []

    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
    pygame.display.update()
    clock.tick(60)