

import sys, pygame, random
from pygame.locals import *
from Objs import char,keyboard,mouse

def writeStrings(surface):		
	stackSpot = 10
	for string in char.getStringS():
		location = write(string,(100,stackSpot),16)
		surface.blit(location[0],location[1])
            ##print str(Sspot)
		stackSpot += 20
	char.clearStackData()

def write(string = 'default_string',loc = (90,90),size=20,font='freesansbold.ttf',color='black'):
    
	BASICFONT = pygame.font.Font(font, size)
	textSurface = BASICFONT.render(str(string), True, Color(color),None)
	textRectangle = textSurface.get_rect()
	
	textRectangle.left = loc[0] # width (x axis)
	textRectangle.top = loc[1] #height (y axis) 
	return (textSurface,textRectangle)