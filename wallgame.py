# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://cs.simpson.edu/?q=python_pygame_examples

import pygame
from pygame.locals import *#Color, KEYUP, K_ESCAPE, K_RETURN
pygame.font.init()

black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
stackOStrings = []

def write(string = 'default_string',loc = (90,90),size=20,font='freesansbold.ttf',color='black'):
    
	BASICFONT = pygame.font.Font(font, size)
	textSurface = BASICFONT.render(str(string), True, Color(color),None)
	textRectangle = textSurface.get_rect()
	
	textRectangle.left = loc[0]
	textRectangle.top = loc[1]
	return (textSurface,textRectangle)


# This class represents the bar at the bottom that the player controls
class Wall(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self,x,y,width,height):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(blue)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x


# This class represents the bar at the bottom that the player controls
class Player(pygame.sprite.Sprite):

    # Set speed vector
    change_x=0
    change_y=0

    # Constructor function
    def __init__(self,x,y):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(white)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
        self.list = []

    def setString(self,string):
        self.string = string

    def getString(self):
        return self.string	

    def setStringS(self,string):
        self.list.append(string)

    def getStringS(self):
        return self.list
		
    def clearStackData(self):
        self.list = []
		
    # Change the speed of the player
    def changespeed(self,x,y):
        self.change_x+=x
        self.change_y+=y
        # print "change_y is: " + str(self.change_y)
        # print "change_x is: " + str(self.change_x)		
        # string = "self.change_x is: ", str(self.change_x)
        # self.setStringS(string)
		
    # Find a new position for the player
    def update(self,walls):
        # Get the old position, in case we need to go back to it
        old_x=self.rect.left
        new_x=old_x+self.change_x
        self.rect.left = new_x
		
        sentence = "x is: " + str(self.change_x)
        self.setStringS(sentence)
        sentence = "old_x: " + str(old_x)
        self.setStringS(sentence)
        sentence = "new_x: " + str(new_x)
        self.setStringS(sentence)

        # Did this update cause us to hit a wall?
        collide = pygame.sprite.spritecollide(self, walls, False)
        if collide:
            # Whoops, hit a wall. Go back to the old position
            self.rect.left=old_x

        old_y=self.rect.top
        new_y=old_y+self.change_y
        self.rect.top = new_y
		
        sentence = "---------------" 
        self.setStringS(sentence)
        sentence = "y is: " + str(self.change_y)
        self.setStringS(sentence)
        sentence = "old_y: " + str(old_y)
        self.setStringS(sentence)
        sentence = "new_y: " + str(new_y)
        self.setStringS(sentence)

        # Did this update cause us to hit a wall?
        collide = pygame.sprite.spritecollide(self, walls, False)
        if collide:
            # Whoops, hit a wall. Go back to the old position
            self.rect.top=old_y

    def writeStrings(self):		
        stackSpot = 50
        for string in player.getStringS():
            location = write(string,(500,stackSpot),16)
            screen.blit(location[0],location[1])
            #print str(Sspot)
            stackSpot += 20
        self.clearStackData()

score = 0
# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])

# Set the title of the window
pygame.display.set_caption('Test')

# Create a surface we can draw on
background = pygame.Surface(screen.get_size())

# Used for converting color maps and such
background = background.convert()

# Fill the screen with a black background
background.fill(Color('purple'))

# Create the player paddle object
player = Player( 50,50 )
movingsprites = pygame.sprite.RenderPlain()
movingsprites.add(player)

# Make the walls. (x_pos, y_pos, width, height)
wall_list=pygame.sprite.RenderPlain()
wall=Wall(0,0,10,600)
wall_list.add(wall)
wall=Wall(10,0,790,10)
wall_list.add(wall)
wall=Wall(10,200,100,10)
wall_list.add(wall)

clock = pygame.time.Clock()

done = False

while done == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3,0)
            if event.key == pygame.K_RIGHT:
                player.changespeed(3,0)
            if event.key == pygame.K_UP:
                player.changespeed(0,-3)
            if event.key == pygame.K_DOWN:
                player.changespeed(0,3)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3,0)
            if event.key == pygame.K_RIGHT:
                player.changespeed(-3,0)
            if event.key == pygame.K_UP:
                player.changespeed(0,3)
            if event.key == pygame.K_DOWN:
                player.changespeed(0,-3)

    player.update(wall_list)

    screen.fill(Color('pink'))
	

		
    # sentence = player.getString()
    # location = write(sentence,(600,50),16)
    # screen.blit(location[0],location[1])
    player.writeStrings()
    movingsprites.draw(screen)

    wall_list.draw(screen)
    pygame.display.flip()

    clock.tick(40)

pygame.quit()