from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, LineAsset, PolygonAsset
import math

Colors=[0xFE2712, 0xFC600A, 0xFB9902, 0xFCCC1A, 0xFEFE33, 0xB2D732, 0x66B032, 0x347C98, 0x0247FE, 0x4424D6, 0x8601AF, 0xC21460]
Color1=[Color(q, 1.0) for q in Colors]
Color2=Color(0x000000, 1.0)
BG=Color(0xffffff, 0.0)
numrot=12
radius=300
LC1=[LineStyle(1, r) for r in Color1]
LC2=LineStyle(1, Color2)
LC3=LineStyle(5, Color2)

"""
test=LineAsset(200, 300, LC1)
Sprite(test, (900,300))
test2=LineAsset(900, 300, LC2)
Sprite(test2, (0,0))
"""

circle=CircleAsset((radius), LC2, BG)
center=CircleAsset(10, LC3, BG)
Sprite(circle, (0,0))
Sprite(center, (290,290))

i=0

def radians(ANGLE):
    angle=ANGLE*((2*math.pi)/360)
    return(angle)


while i < (numrot):
    angle=radians((360/numrot)*((i+(numrot/4))%numrot))
    linecoor=[math.cos(angle)*radius,math.sin(angle)*radius]
    line=LineAsset(linecoor[0], linecoor[1], LC1[i])
    print((360/numrot)*((i+(numrot/4))%numrot),linecoor)
    if ((360/numrot)*((i+(numrot/4))%numrot)) >= 0 and ((360/numrot)*((i+(numrot/4))%numrot)) < 90:
         Sprite(line, (300, 300))
    elif ((360/numrot)*((i+(numrot/4))%numrot)) >= 90 and ((360/numrot)*((i+(numrot/4))%numrot)) < 180:
        Sprite(line, (300+(math.cos(angle)*300), 300))
    elif ((360/numrot)*((i+(numrot/4))%numrot)) >= 180 and ((360/numrot)*((i+(numrot/4))%numrot)) < 270:
        Sprite(line, (300+(math.cos(angle)*300), 300+(math.sin(angle)*300)))
    elif ((360/numrot)*((i+(numrot/4))%numrot)) >= 270 and ((360/numrot)*((i+(numrot/4))%numrot)) < 360:
        Sprite(line, (300, 300+(math.sin(angle)*300)))
    NUMBER=LineAsset(100,250, LC1[i])
    Sprite(NUMBER, (600+(50*i),500))
    i=i+1

DrawSigil = App()
DrawSigil.run()
