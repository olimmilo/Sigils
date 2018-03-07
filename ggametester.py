from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, LineAsset, PolygonAsset

Color1=Color(0x000000, 1.0)
Color2=Color(0x0000FF, 1.0)

LC1=LineStyle(1, Color1)
LC2=LineStyle(1, Color2)

test=LineAsset(200, 300, LC1)
Sprite(test, (900,300))
test2=LineAsset(900, 300, LC2)
Sprite(test2, (0,0))

DrawSigil = App()
DrawSigil.run()
