from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, LineAsset, PolygonAsset

import math


def sqrt(NUM):
    SQRT=NUM**0.5
    return(SQRT)
    
def radians(ANGLE):
    angle=ANGLE*((2*math.pi)/360)
    return(angle)
    
def degrees(ANGLE):
    angle=ANGLE*(360/(2*math.pi))
    return(angle)


#go here https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Programmed-Graphics

Rot = 60
Shift = 40
Canvas = 550
Buffer = 20
Colors=[0xFE2712, 0xFC600A, 0xFB9902, 0xFCCC1A, 0xFEFE33, 0xB2D732, 0x66B032, 0x347C98, 0x0247FE, 0x4424D6, 0x8601AF, 0xC21460]
Color1=Color(0x000000, 1.0)
Color2=Color(0x993399, 1.0)
Center=[.5,.5]
Radius=.5


def Intersect(ANGLE):
	COOR=[-1,-1]
	ANGLE=ANGLE%360
	LEN=COOR[0]
	r=0.5
	j=Center[0]
	k=Center[1]
	m=(math.tan(radians(ANGLE)))
	n=LEN
	if ANGLE == 0:
		COOR=[1,.5]
	elif ANGLE == 90:
		COOR=[.5,1]
	elif ANGLE == 180:
		COOR=[0,.5]
	elif ANGLE == 270:
		COOR=[.5,0]
	elif ANGLE > 0 and ANGLE < 90:
		COOR[0]=(((m**2)*j)+j+(r*sqrt((m**2)+1)))/((m**2)+1)
		COOR[1]=m*(COOR[0]-j)+k
	elif ANGLE > 90 and ANGLE < 180:
		COOR[0]=(((m**2)*j)+j-(r*sqrt((m**2)+1)))/((m**2)+1)
		COOR[1]=m*(COOR[0]-j)+k
	elif ANGLE > 180 and ANGLE < 270:
		COOR[0]=(((m**2)*j)+j-(r*sqrt((m**2)+1)))/((m**2)+1)
		COOR[1]=m*(COOR[0]-j)+k
	elif ANGLE > 270 and ANGLE < 360:
		COOR[0]=(((m**2)*j)+j+(r*sqrt((m**2)+1)))/((m**2)+1)
		COOR[1]=m*(COOR[0]-j)+k
	if COOR[0] < 0 or COOR[1] < 0:
	    print("you done fucked up")
	return(COOR)

def Angle(ITERATION):
    ANGLE=(ITERATION*120)%360
    return(ANGLE)

def LineList(ITERATION, ROT, SHIFT):
    line=[]
    line.append([Intersect((Angle(ITERATION))+ROT),Intersect((Angle((ITERATION-1)%3)-SHIFT)+ROT)])
    line.append([Intersect((Angle(ITERATION))+ROT),Intersect((Angle((ITERATION+1)%3)+SHIFT)+ROT)])
    line.append([Intersect((Angle(ITERATION)+SHIFT)+ROT),Intersect((Angle(ITERATION)-SHIFT)+ROT)])
    return(line)

def DrawSymbol(ROT, SHIFT, CANVAS, BUFFER, COLOR1, COLOR2):
	SCALE=CANVAS-BUFFER
	PAD=BUFFER/2
	LINELIST=[]
	LC1=LineStyle(8, COLOR2)
	LC2=LineStyle(8, COLOR2)
	BG=Color(0xffffff, 0.0)
	SCREEN=RectangleAsset(CANVAS, CANVAS, LC1, BG)
	CIRCLE=CircleAsset((Radius*SCALE), LC1, Color(0x993399, 0.05))
	#Sprite(SCREEN, (0,0))
	Sprite(CIRCLE, (PAD,PAD))
	i=0
	while i <= 2:
		list=LineList(i, ROT, SHIFT)
		LINELIST.extend(list)
		list=[]
		i=i+1
	n=0
	while n < len(LINELIST):
		LC1=LineStyle(4, Color(0x993399, 0.75))
		LINELIST[n][0]=[(e*SCALE)+PAD for e in LINELIST[n][0]]
		LINELIST[n][1]=[(j*SCALE)+PAD for j in LINELIST[n][1]]
		line=LINELIST[n]
		slope=(degrees(math.atan((line[1][1]-line[0][1])/(line[1][0]-line[0][0]))))%360
		rslope=(math.atan((line[1][1]-line[0][1])/(line[1][0]-line[0][0])))%(2*math.pi)
		hypot=(line[1][0]-line[0][0])/(math.cos(rslope))
		if slope == 0 or slope == 360:
		    TEMPline=LineAsset((line[1][0]-line[0][0]),(line[1][1]-line[0][1]), LC1)
		    Sprite(TEMPline, (line[0][0], line[0][1]))
		    if line[0][0] > line[1][0]:
		        Sprite(TEMPline, (line[1][0], line[0][1]))
		    else:
		        Sprite(TEMPline, (line[0][0], line[0][1]))

		elif slope == 90 or slope == 270:
		    TEMPline=LineAsset((line[1][0]-line[0][0]),(line[1][1]-line[0][1]), LC1)
		    if line[0][1] > line[1][1]:
		        Sprite(TEMPline, (line[0][0], line[1][1]))
		    else:
		        Sprite(TEMPline, (line[0][0], line[0][1]))
		else:
		    TEMPline=LineAsset((line[1][0]-line[0][0]),(line[1][1]-line[0][1]), LC1)
		if slope > 0 and slope < 90:
			if line[0][0] > line[1][0]:
				Sprite(TEMPline, (line[1][0], line[1][1]))
			else:
				Sprite(TEMPline, (line[0][0], line[0][1]))
		elif slope > 90 and slope < 180:
			if line[0][0] > line[1][0]:
				Sprite(TEMPline, (line[1][0]+(math.cos(rslope)*hypot), line[1][1]))
			else:
				Sprite(TEMPline, (line[0][0]+(math.cos(rslope)*hypot), line[0][1]))
		elif slope > 180 and slope < 270:
			if line[0][0] > line[1][0]:
				Sprite(TEMPline, (line[1][0]+(math.cos(rslope)*hypot), line[1][1]-(math.sin(rslope)*hypot)))
			else:
				Sprite(TEMPline, (line[0][0]+(math.cos(rslope)*hypot), line[0][1]+(math.sin(rslope)*hypot)))
		elif slope > 270 and slope < 360:
			if line[0][0] > line[1][0]:
				Sprite(TEMPline, (line[1][0], line[1][1]-(math.sin(rslope)*hypot)))
			else:
				Sprite(TEMPline, (line[0][0], line[0][1]+(math.sin(rslope)*hypot)))
		
		#Sprite(TEMPline, (line[0][0],line[0][1]))
		n=n+1

	LC1=LineStyle(8, COLOR2)
	CIRCLE=CircleAsset((Radius*SCALE), LC1, BG)
	Sprite(CIRCLE, (PAD,PAD))
	return(LINELIST)

def DrawSubSymbol(ROT, SHIFT, CANVAS, BUFFER, COLOR1, COLOR2):
	SCALE=CANVAS-BUFFER
	PAD=BUFFER/2
	LINELIST=[]
	LC1=LineStyle(4, COLOR1)
	LC2=LineStyle(4, COLOR2)
	BG=Color(0xffffff, 0.0)
	
	SEC=LineList(1, 0, SHIFT)
	HEAD=Intersect(Angle(1)+180)
	
	RADIUS=.125
	
	CIRCLE=CircleAsset((RADIUS*SCALE), LC2, BG)
	Sprite(CIRCLE, ((CANVAS/2)-((RADIUS*SCALE)),(CANVAS/2)-((RADIUS*SCALE))))
	i=0
	while i<3:
	    i=i+1
	return()
DrawSymbol(Rot, Shift, Canvas, Buffer, Color1, Color2)

#DrawSubSymbol(Rot, Shift, Canvas, Buffer, Color1, Color2)

DrawSigil = App()
DrawSigil.run()
