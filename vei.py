from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, LineAsset, PolygonAsset

import math

#go here https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Programmed-Graphics

Rot = 0
Shift = 40
Canvas = 500
Buffer = 0
Color1=Color(0x000000, 1.0)
Color2=Color(0x993399, 1.0)
Center=[.5,.5]
Radius=.5


def sqrt(NUM):
    SQRT=NUM**0.5
    return(SQRT)
    
def radians(ANGLE):
    angle=ANGLE*((2*math.pi)/360)
    return(angle)

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
	LC1=LineStyle(1, COLOR1)
	LC2=LineStyle(1, COLOR2)
	BG=Color(0xffffff, 0.0)
	SCREEN=RectangleAsset(CANVAS, CANVAS, LC1, BG)
	CIRCLE=CircleAsset((Radius*SCALE), LC1, BG)
	Sprite(SCREEN, (0,0))
	Sprite(CIRCLE, (PAD,PAD))
	i=0
	while i <= 2:
	    list=LineList(i, ROT, SHIFT)
	    LINELIST.extend(list)
	    list=[]
	    i=i+1
	n=0
	while n < len(LINELIST):
	    LINELIST[n][0]=[(e*SCALE)+PAD for e in LINELIST[n][0]]
	    LINELIST[n][1]=[(j*SCALE)+PAD for j in LINELIST[n][1]]
	    line=LINELIST[n]
	    TEMPpol=PolygonAsset([tuple(line[0]),tuple(line[1]),tuple(line[0])], LC1, BG)
	    Sprite(TEMPpol, (0,0))
	    #TEMPline=LineAsset((line[1][0]-line[0][0]),(line[1][1]-line[0][1]), LC1)
	    #Sprite(TEMPline, ((line[0][0]+line[1][0])/2,(line[0][1]+line[1][1])/2))
	    n=n+1

	return(LINELIST)

lisy=DrawSymbol(Rot, Shift, Canvas, Buffer, Color1, Color2)

g=0

print(lisy)
print()
while g < len(lisy):
    h=0
    while h < len(lisy[g]):
        print(lisy[g][h][0],lisy[g][h][1])
        h=h+1
    g=g+1

DrawSigil = App()
DrawSigil.run()
