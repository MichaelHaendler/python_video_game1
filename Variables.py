
import sys, pygame, random

#########START OF VARIABLES####################################################################

numb = 96
yVal = 48

height = 46
h_back = height * 1.1 * 1.95 * 1.47
h_right = height * 1.1 * 1.95
h_left = height * 1.1

gunTorImageSqs = (
(0,0,100,100),
(150,0, 100, 100),
(260,0,120,120),
(350,0,100,100),
(0,100,100,120),
(100,100,130,130),
(230,100,130,130),
(330,100,130,130)
)

gun_center = [10,10]
gun_x = 50
gun_y = 50

gun_center[0] += gun_x
gun_center[1] += gun_y

gunTorShps = (
[gun_center,(75+gun_x,0+gun_y),(125+gun_x,0+gun_y)],#0
[gun_center,(125+gun_x,0+gun_y),(200+gun_x,75+gun_y)],#1
[gun_center,(200+gun_x,75+gun_y),(200+gun_x,125+gun_y)],#2
[gun_center,(200+gun_x,125+gun_y),(125+gun_x,200+gun_y)],#3
[gun_center,(125+gun_x,200+gun_y),(75+gun_y,200+gun_y)],#4
[gun_center,(75+gun_x,200+gun_y),(0+gun_x,125+gun_y)],#5
[gun_center,(0+gun_x,125+gun_y),(0+gun_x,75+gun_y)],#6
[gun_center,(0+gun_x,75+gun_y),(75+gun_x,0+gun_y)],#7
)
fileLoc = 'tower.png'
torSquare = pygame.Rect(90,90,90,90)

firstTime = True
old_tup = ()
new_tup = (0,0)
done = False
surface = pygame.display.set_mode((550,500))
tupSurface = (0,0,surface.get_width,surface.get_height)


inside = False
theColor = "red"
FPS = 120
speed = 14
frames = FPS / speed
width = 1
center = [150,200]
#can be used to move the octogon
shift_x = 20
shift_y = 20


expand = 1.7 #2.5
#height and offset are very much used in the code
height = 50 * expand
offset = 20 * expand
oct_x = center[0]
oct_y = center[1]
point1 = (oct_x - offset,oct_y - height)
point2 = (oct_x + offset,oct_y - height)
tempRect = surface.get_rect()

centert = [150,200]

point1t = (oct_x + offset,oct_y + height)
point2t = (oct_x - offset,oct_y + height)
rectt = pygame.Rect(0,0,26,45)

points = {
'0':((oct_x - offset,oct_y - height),(oct_x+offset,oct_y-height)),
'1':((oct_x + offset,oct_y - height),(oct_x+height,oct_y-offset)),
'2':((oct_x+height,oct_y-offset),(oct_x+height,oct_y+offset)),
'3':((oct_x+height,oct_y+offset),(oct_x + offset,oct_y + height)),
'4':((oct_x + offset,oct_y + height),(oct_x - offset,oct_y + height)),
'5':((oct_x - offset,oct_y + height),(oct_x - height,oct_y + offset)),
'6':((oct_x - height,oct_y + offset),(oct_x - height,oct_y - offset)),
'7':((oct_x - height,oct_y - offset),(oct_x - offset,oct_y - height))
}


imageSquare = {
'0':(37,141,45,75),
'1':(377,32,68,65),
'2':(258,38,91,59),
'3':(145,35,78, 63),

'4':(38,38,42,61),
'5':(366,154,77,62),
'6':(239,156,91,60),

'7':(141,150,68,67),
}

#########END OF VARIABLES####################################################################