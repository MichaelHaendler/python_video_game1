
from Variables import * 
from GunTor2 import GunTor
from SingleTri import Shape, Shapes
from Person import Person
from Movement import Keyboard,Mouse,Input
from Button import Button
from WalkingGUI import WalkingGUI
from WriteToSurface import Write,Squares
from StartScreen import StartScreen
from Item import Item
from BackPack import BackPack
from itemHolder import ItemHolder

char = Person()
char.sizeOfload(4)

char.load('queen.png',[(0,0,30,50),(35,0, 30, 50),(65,0,30,50)],3,'front','king',-1,True,frames)
char.load('queen.png',[(0,h_left,30,height),(35,h_left, 30, height),(65,h_left,30,height)],3,'left','king',-1,True,frames)
char.load('queen.png',[(0,h_right,30,height),(35,h_right, 30, height),(65,h_right,30,height)],3,'right','king',-1,True,frames)
char.load('queen.png',[(0,h_back,30,height),(35,h_back, 30, height),(65,h_back,30,height)],3,'back','king',-1,True,frames)

char.sizeOfload(4)

char.load('queen.png',[(numb + 0, yVal*4,30,50),(numb + 35, yVal*4, 30, 50),( numb + 65, yVal*4,30,50)],3,'front','armor',-1,True,frames)
char.load('queen.png',[(numb + 0, yVal*5,30,50),(numb + 35, yVal*5, 30, 50),( numb + 65, yVal*5,30,50)],3,'left','armor',-1,True,frames)
char.load('queen.png',[(numb + 0, yVal*6,30,50),(numb + 35, yVal*6, 30, 50),( numb + 65, yVal*6,30,50)],3,'right','armor',-1,True,frames)
char.load('queen.png',[(numb + 0, yVal*7,30,50),(numb + 35, yVal*7, 30, 50),( numb + 65, yVal*7,30,50)],3,'back','armor',-1,True,frames)

char.setWhichChar('armor')
char.setX(42)
char.setY(320)


tris = Shapes(center,points,tempRect,imageSquare,'tower.png')


#trit = Shape(centert,point1t,point2t,rectt,rectt,"left","tower.png")
trit = Shape(centert,point1t,point2t,tempRect,(0,0,0,0),"right","tower.png")

# sq = Button(250,50)

keyboard = Keyboard()
mouse = Mouse()
inputted = Input()
printS = Write()

menu = StartScreen(surface.get_width(),surface.get_height())

tup = ["tankPic.png",surface.get_rect(),(0,0)]
menu.placeAt("background",tup)

tup=["buttons.png","game",(0,30,117,25),(0,0,120,30),(250,200)]
menu.placeAt("button",tup)

tup = ["falloutBox.jpeg",(0,0,320,150),(50,10)]
menu.placeAt("background",tup)

menu.makeBasicScreen()

fruit = Item(200,100)
fruit.setImage("items.png",pygame.Rect(0,0,31,31))


button = Button()
button.setOffImage("buttons.png",(0,0,120,20))
button.setOnImage("buttons.png",(0,32,115,25))
button.setLoc(130,50)
button.setName("exit")

bar = Button()
bar.setOffImage("userBar.png",(0,0,349,17))
bar.setOnImage("userBar.png",(0,0,349,17)) # note: you may want to have 2 different bars. One clicked, one not clicked. 
bar.setLoc(0,0)
bar.setName("userBar")

inventory = BackPack(width = 230, height = 200)
inventory.addPreMadeButton(bar)
inventory.addPreMadeButton(button)
inventory.setLoc(203,292)
#inventory.setImage("city.png",(0,0),(20,20,100,100))#works! 
inventory.fill("purple.png")
#print "only here once" 
inventory.makeBasicMenu()
inventory.clicked = True

itemColumn = ItemHolder()
itemColumn.setBackground_fileName("item_column_background.png")
itemColumn.makeBasicInventory()
itemColumn.setLoc(100,250)

