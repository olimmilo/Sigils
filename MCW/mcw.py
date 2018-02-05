from PIL import Image, ImageDraw

scale=100
s=scale
width=20*s
height=20*s

imtop = Image.new("RGB", (width,height), "white")
immid = Image.new("RGB", (width,height), "white")
drawtop = ImageDraw.Draw(imtop)
drawmid = ImageDraw.Draw(immid)

##top def
drawtop.line((4.879*s,4.879*s,15.707*s,15.707*s), width=1, fill="black")
drawtop.line((4*s,7*s,10*s,7*s),width=1, fill="black")
drawtop.line((7*s,4*s,7*s,13*s),width=1, fill="black")
drawtop.line((7*s,13*s,8*s,13*s),width=1, fill="black")
drawtop.line((8*s,9.828*s,8*s,15.236*s),width=1, fill="black")
drawtop.line((8*s,10.764*s,10*s,10.764*s),width=1, fill="black")
drawtop.line((8*s,15.236*s,10*s,15.236*s),width=1, fill="black")
drawtop.line((10*s,10*s,10*s,16*s),width=1, fill="black")
drawtop.line((10*s,10*s,16*s,10*s),width=1, fill="black")
drawtop.line((10*s,13*s,13*s,10*s),width=1, fill="black")
drawtop.line((13*s,10*s,13*s,16*s),width=1, fill="black")
drawtop.line((16*s,9*s,16*s,15*s),width=1, fill="black")
drawtop.line((10*s,16*s,15*s,16*s),width=1, fill="black")
drawtop.line((15*s,14*s,15*s,16*s),width=1, fill="black")
drawtop.line((14*s,15*s,16*s,15*s),width=1, fill="black")
drawtop.line((15*s,14*s,16*s,13*s),width=1, fill="black")
drawtop.line((14*s,15*s,13*s,16*s),width=1, fill="black")
drawtop.line((10*s,8*s,14.5*s,8*s),width=1, fill="black")
drawtop.line((10*s,7*s,10,9*s),width=1, fill="black")

##makes imbot
imbot = imtop

imtop.show()
