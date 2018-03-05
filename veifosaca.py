from PIL import Image, ImageDraw

Rot = 0
Shift = 40
Canvas = 1000
Buffer = 100

def Intersect(CENTER, ANGLE, RADIUS):
	COOR=[.5,.5]
	a=ANGLE^2
	b=(-2*CENTER[0])-((ANGLE^2)*CENTER[0])
	c=((ANGLE^2)*CENTER[0])+(CENTER[0]^2)-(RADIUS^2)
	ANGLE=ANGLE%360
	if b != .5:
		print("wrong b")
	if ANGLE == 0:
		COOR=[.5,1]
	elif ANGLE == 90:
		COOR=[1,.5]
	elif ANGLE == 180:
		COOR=[.5,0]
	elif ANGLE == 270:
		COOR=[0,.5]
	elif ANGLE > 0 and ANGLE < 90:
		COOR[0]=(-b+sqrt((b^2)-(4*a*c)))/(2*a)
		COOR[1]=(ANGLE*(COOR[0]-CENTER[0]))+CENTER[1]
	elif ANGLE > 90 and ANGLE < 180:
		COOR[0]=(-b-sqrt((b^2)-(4*a*c)))/(2*a)
	elif ANGLE > 180 and ANGLE < 270:
		COOR[0]=(-b-sqrt((b^2)-(4*a*c)))/(2*a)
	elif ANGLE > 270 and ANGLE < 0:
		COOR[0]=(-b+sqrt((b^2)-(4*a*c)))/(2*a)
	return(COOR)

def DrawSymbol(ROT, SHIFT, CANVAS, BUFFER):
	Center=[.5,.5]
	return()

symbol = Image.new("RGB", (Canvas,Canvas), "white")
drawsymbol = ImageDraw.Draw(symbol)

DrawSymbol(Rot, Shift, Canvas, Buffer)

symbol.show()
