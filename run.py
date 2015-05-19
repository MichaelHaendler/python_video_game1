#ctrl Q will remove pound signs
#ctrl K will add pound signs 

#this video game was created by Michael Joseph Haendler

import sys, pygame, random
from pygame.locals import *#Color, KEYUP, K_ESCAPE, K_RETURN
import spritesheet
from sprite_strip_anim import SpriteStripAnim
#########
from Person import Person
from GunTor2 import GunTor
from SingleTri import Shape, Shapes
from Movement import Mouse, Keyboard, Input
from Button import Button
from Variables import * 
from WriteToGUI import writeStrings, write
from Objs import *
import Objs2
import math
from WalkingGUI import WalkingGUI, Circle
from Menu import Square,Squares,Menu # to be deleted after testing?
from WriteToSurface import Square

pygame.font.init()

clock = pygame.time.Clock()

wall_list = []
#wall_list.append(sq.getRect())

while done == False:

	surface.fill(Color('pink'))
	
	for event in pygame.event.get():

		map = keyboard.moved(event)
		map = mouse.appendMouseActions(map,event)
		
		if menu.getSelection() == "game":
			char.move(map)
			
	if map['K_QUIT'] == True:
		done = True
			
	if map['K_ESCAPE'] == True or menu.stayOpen(map) == True:
		tempyMenu = menu.getScreen(map)
		surface.blit(tempyMenu[0],tempyMenu[1])
	
	if menu.getSelection() == "game":
				
		fruit.move(map)
		# sq.change(mouse.mouseActions(event))
		# pygame.draw.rect(surface,sq.getColor(),sq.getRect(),sq.getThickness())
		
		if inventory.show():
			surface.blit(inventory.getBackPack(map),inventory.getLoc())
		
		
		itemColumn.holding(fruit,map)
		
		surface.blit(itemColumn.getInventoryImage(),itemColumn.getLoc())
		
		surface.blit(fruit.image,fruit.getLoc())
		
		for name in tris.getNames():
			tempShape = tris.getShape(name)
			if tempShape.contains(char):
				tempShape.setColor("green")
				surface.blit(tempShape.getImage(),tris.getCenter(name))
			else:
				tempShape.setColor("black")
			pygame.draw.lines(surface,tempShape.getColor(),True,tempShape.pointList(),width)
			
		char.update(wall_list)
		surface.blit(char.updateScreen(map,surface),(0,0))##one of char's most important lines in run
		
##################################################		
		sentence = "mice: " + str(mouse.getLoc())
		Objs2.tempSqs.add(sentence)
		sentence ="char: " + str(char.getRect())	
		Objs2.tempSqs.add(sentence)		
			
		loc1 = 0 #over
		loc2 = 0 #down
		for squ in Objs2.tempSqs.getSquares():
			surface.blit(squ.getSurface(),(loc1,loc2))
			loc2 += 30
		Objs2.tempSqs.clear()
		
	pygame.display.flip()
	
	clock.tick(120/6)

