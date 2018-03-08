from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, LineAsset, PolygonAsset
import math

Colors=[0xFE2712, 0xFC600A, 0xFB9902, 0xFCCC1A, 0xFEFE33, 0xB2D732, 0x66B032, 0x347C98, 0x0247FE, 0x4424D6, 0x8601AF, 0xC21460]
Color1=[Color(q, 1.0) for q in Colors]
Color2=Color(0x0000FF, 1.0)

LC1=[LineStyle(1, r) for r in Color1]

"""
test=LineAsset(200, 300, LC1)
Sprite(test, (900,300))
test2=LineAsset(900, 300, LC2)
Sprite(test2, (0,0))
"""
numrot=12
radius=500
i=0

def radians(ANGLE):
    angle=ANGLE*((2*math.pi)/360)
    return(angle)


while i < 12:
    angle=radians((360/numrot)*((i+(numrot/4))%numrot))
    linecoor=[math.cos(angle)*radius,math.sin(angle)*radius]
    line=LineAsset(linecoor[0], linecoor[1], LC1[i])
    Sprite(line, (500, 500))
    i=i+1

DrawSigil = App()
DrawSigil.run()
