

import sys, pygame, random
from pygame.locals import *#Color, KEYUP, K_ESCAPE, K_RETURN


class Input:

	def __init__(self):
		self.mouse = Mouse()
		self.keyboard = Keyboard()
		
	def thingsPressed(self,event):
		map = self.keyboard.moved(event)
		map = self.mouse.appendMouseActions(map,event)
		return map

class Keyboard:

	def __init__(self):
		self.no_reason = 0
		
		
	def moved(self,event):
		map = {'type':'UP_DOWN','K_ESCAPE':False,'K_QUIT':False,'K_ESCAPE':False,'K_RIGHT':False,'K_LEFT':False,'K_UP':False,'K_DOWN':False}
		
		if event.type == pygame.QUIT:
			map['K_QUIT'] = True
			
		if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
		
			if event.type == pygame.KEYDOWN:
				map['type'] = 'KEYDOWN'

			if event.type == pygame.KEYUP:
				map['type'] = 'KEYUP'
				
			if event.key == pygame.K_ESCAPE:
				map['K_ESCAPE'] = True
				
			if event.key == pygame.K_LEFT:
				map['K_LEFT'] = True
				
			if event.key == pygame.K_RIGHT:
				map['K_RIGHT'] = True
				
			if event.key == pygame.K_UP:
				map['K_UP'] = True
				
			if event.key == pygame.K_DOWN:
				map['K_DOWN'] = True
			
		return map

class Mouse:

	def __init__(self):
		self.map = {}
		self.map['coords'] = (0,0)
		self.map['button'] = 'neither' 
		self.map['button1'] = False
		self.map['button2'] = False
		self.map['button3'] = False
		self.mouseTup = (0,0)
		
	def getLoc(self):
		return pygame.mouse.get_pos()

	def mouseActions(self,event):
		
		if event.type == MOUSEMOTION:
			self.map['coords'] = pygame.mouse.get_pos()
			self.mouseTup = self.map['coords']
			
		if event.type != MOUSEMOTION:
			self.map['coords'] = self.mouseTup
			
		if event.type == MOUSEBUTTONDOWN:
			self.map['button'] = 'down'
			button = event
			#button = pygame.event.wait()
			if button.button == 1:
				self.map['button1'] = True
			if button.button == 2:
				self.map['button2'] = True
			if button.button == 3:
				self.map['button3'] = True
				
		if event.type == MOUSEBUTTONUP:
			self.map['button'] = 'up' 

				
		return self.map
		
	def appendMouseActions(self,map,event):
	
		map['coords'] = (0,0)
		map['button'] = 'neither' 
		map['button1'] = False
		map['button2'] = False
		map['button3'] = False
		
		if event.type == MOUSEMOTION:
			map['coords'] = pygame.mouse.get_pos()
			self.mouseTup = map['coords']
			
		if event.type != MOUSEMOTION:
			map['coords'] = self.mouseTup
			
		if event.type == MOUSEBUTTONDOWN:
			map['button'] = 'down'
			button = event
			#button = pygame.event.wait()
			if button.button == 1:
				map['button1'] = True
			if button.button == 2:
				map['button2'] = True
			if button.button == 3:
				map['button3'] = True
				
		if event.type == MOUSEBUTTONUP:
			map['button'] = 'up' 

				
		return map

		