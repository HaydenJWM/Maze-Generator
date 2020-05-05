#Implimentation of depth first maze generation algorithm in python via pygame
#Needs signifigant refactoring
#Make it so that the maze is generated via wall removal
import pygame
import random

#Global variables
pygame.init()
screen_width = 500
screen_height = 500
block_size = 25
screen = pygame.display.set_mode((screen_width,screen_height))

#Class to hold the maze blocks
class Block:
    def __init__(self,x,y):
        self.x = x
        self.y = y 
        self.visited = False

    def print(self):
        print("Position: (",self.x,",",self.y,")")
    
    def remove_left(self):
        pygame.draw.line(screen,(0,0,0),(self.x,self.y),(self.x,self.y+block_size),1)

    def remove_right(self):
        pygame.draw.line(screen,(0,0,0),(self.x+block_size,self.y),(self.x+block_size,self.y+block_size),1)

    def remove_up(self):
        pygame.draw.line(screen,(0,0,0),(self.x,self.y),(self.x+block_size,self.y),1)

    def remove_down(self):
        pygame.draw.line(screen,(0,0,0),(self.x,self.y+block_size),(self.x+block_size,self.y+block_size),1)

#Draws base grid
def grid():
    for x in range(0,screen_width,block_size):
        pygame.draw.line(screen,(255,255,255),(x,0),(x,screen_height),1)
    for y in range(0,screen_height,block_size):
        pygame.draw.line(screen,(255,255,255),(0,y),(screen_width,y),1)

#Populate block list
def makeBlocks():
    blockList = []

    #Loop over and make block objects
    for x in range(0,screen_width,block_size):
        innerBlocks = []
        for y in range(0,screen_height,block_size):
            newBlock = Block(x,y)
            innerBlocks.append(newBlock)
        blockList.append(innerBlocks)

    return blockList

#Prints the contents of the grid to the screen
def printGrid(grid):
    for x in range(0,len(grid)):
        for y in range(0,len(grid[x])):
            grid[x][y].print()

#Recursive depth first maze generation algorithm
def mazeGen(blocks,x,y):
    #Set maze to visited
    blocks[x][y].visited = True

    #Make a direction list, randomize it, then iterate over the list to check all of the blocks
    d = []
    if x != 0:
        d.append((x-1,y))
    if x != len(blocks)-1:
        d.append((x+1,y))
    if y != 0:
        d.append((x,y-1))
    if y != len(blocks)-1:
        d.append((x,y+1))
    random.shuffle(d)

    #Iterate over direction list, skip if the block has been visited, recursivey call on all new blocks
    for (xdir,ydir) in d:
        if blocks[xdir][ydir].visited == True:
            continue
        if  xdir == x:
            if ydir > y:
                blocks[x][y].remove_down()
            else:
                blocks[x][y].remove_up()
        elif ydir == y:
            if xdir > x:
                blocks[x][y].remove_right()
            else:
                blocks[x][y].remove_left()
        mazeGen(blocks,xdir,ydir)

#Main function
def main():
    #Seed random
    random.seed()
    #Draw initial grid
    grid()
    #Get the grid locations where the blocks are located
    blocks = makeBlocks()
    #Testing print
    printGrid(blocks)
  
    #Start maze generation
    mazeGen(blocks,random.randint(0,19),random.randint(0,19))
    
    #Main loop
    while True:
        #Exit window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #Update display
        pygame.display.update()

#Call main function
if __name__ == "__main__":
    main()