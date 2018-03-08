import math

Rot = 0
Shift = 40
Canvas = 100
Buffer = 0
Center=[.5,.5]
Radius=.5
GreaterRes=100
LesserRes=
zInnerRadius=
zOuterRadius=

def sqrt(NUM):
    SQRT=NUM**0.5
    return(SQRT)
    
def radians(ANGLE):
    angle=ANGLE*((2*math.pi)/360)
    return(angle)
    
def degrees(ANGLE):
    angle=ANGLE*(360/(2*math.pi))
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

def DrawInit2d(ROT, SHIFT, CANVAS, BUFFER):
	SCALE=CANVAS-BUFFER
	PAD=BUFFER/2
	LINELIST=[]
	i=0
	while i <= 2:
		list=LineList(i, ROT, SHIFT)
		LINELIST.extend(list)
		list=[]
		i=i+1
	return(LINELIST)

Coordinates=DrawInit2d(Rot, Shift, Canvas, Buffer)
