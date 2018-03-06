from PIL import Image, ImageDraw

Rot = 0
Shift = 40
Canvas = 1000
Buffer = 100
Color1="#000000"
Color2="#993399"
CENTER=[.5,.5]
RADIUS=.5

symbol = Image.new("RGB", (Canvas,Canvas), "white")
drawsymbol = ImageDraw.Draw(symbol)

def sqrt(NUM):
    SQRT=NUM**0.5
    return(SQRT)

def Intersect(ANGLE):
	COOR=[.5,.5]
	ANGLE=ANGLE%360
	LEN=COOR[0]
	j=CENTER[0]
	k=CENTER[1]
	m=ANGLE
	n=LEN
	if ANGLE == 0:
		COOR=[.5,1]
	elif ANGLE == 90:
		COOR=[1,.5]
	elif ANGLE == 180:
		COOR=[.5,0]
	elif ANGLE == 270:
		COOR=[0,.5]
	elif ANGLE > 0 and ANGLE < 90:
		COOR[0]=((j+((m**2)*j))+(n*sqrt(1+(m**2))))/(1+(m**2))
		COOR[1]=m*(COOR[0]-j)+k
	elif ANGLE > 90 and ANGLE < 180:
		COOR[0]=((j+((m**2)*j))+(n*sqrt(1+(m**2))))/(1+(m**2))
		COOR[1]=m*(COOR[0]-j)+k
	elif ANGLE > 180 and ANGLE < 270:
		COOR[0]=((j+((m**2)*j))+(n*sqrt(1+(m**2))))/(1+(m**2))
		COOR[1]=m*(COOR[0]-j)+k
	elif ANGLE > 270 and ANGLE < 0:
		COOR[0]=((j+((m**2)*j))+(n*sqrt(1+(m**2))))/(1+(m**2))
		COOR[1]=m*(COOR[0]-j)+k
	return(COOR)

def Angle(ITERATION):
    ANGLE=(0*120)%360
    return(ANGLE)

def LineList(ITERATION, ROT, SHIFT):
    line=[]
    line.append([Intersect((Angle(ITERATION))+ROT),Intersect((Angle((ITERATION-1)%2)-SHIFT)+ROT)])
    line.append([Intersect((Angle(ITERATION))+ROT),Intersect((Angle((ITERATION+1)%2)+SHIFT)+ROT)])
    line.append([Intersect((Angle(ITERATION)+SHIFT)+ROT),Intersect((Angle(ITERATION)-SHIFT)+ROT)])
    return(line)

def DrawSymbol(ROT, SHIFT, CANVAS, BUFFER, COLOR1, COLOR2)
	SCALE=CANVAS-BUFFER
	PAD=BUFFER/2
	LINELIST=[]
	i=0
	while i <= 2:
	    list=LineList(i, ROT, SHIFT)
	    LINELIST.extend(list)
	    list=[]
	    i=i+1
	n=0
	while n < len(LINELIST):
	    drawsymbol.line((((LINELIST[i][0][0])*SCALE)+PAD,((LINELIST[i][0][1])*SCALE)+PAD,((LINELIST[i][1][0])*SCALE)+PAD,((LINELIST[i][1][1])*SCALE)+PAD), width=1, fill=COLOR1)
	    n=n+1
	return()

DrawSymbol(Rot, Shift, Canvas, Buffer, Color1, Color2)

symbol.show()
