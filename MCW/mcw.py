from PIL import Image, ImageDraw


width=20
height=20

imtop = Image.new("RGB", (width,height), "white")
immid = Image.new("RGB", (width,height), "white")
drawtop = ImageDraw.Draw(imtop)
drawmid = ImageDraw.Draw(immid)

##top def
drawtop.line((4.879,4.879,15.707,15.707), width=1, fill=black)
drawtop.line((4,7,10,7),width=1, fill=black)
drawtop.line((7,4,7,13),width=1, fill=black)
drawtop.line((7,13,8,13),width=1, fill=black)
drawtop.line((8,9.828,8,15.236),width=1, fill=black)
drawtop.line((8,10.764,10,10.764),width=1, fill=black)
drawtop.line((8,15.236,10,15.236),width=1, fill=black)
drawtop.line((10,10,10,16),width=1, fill=black)
drawtop.line((10,10,16,10),width=1, fill=black)
drawtop.line((10,13,13,10),width=1, fill=black)
drawtop.line((13,10,13,16),width=1, fill=black)
drawtop.line((16,9,16,15),width=1, fill=black)
drawtop.line((10,16,15,16),width=1, fill=black)
drawtop.line((15,14,15,16),width=1, fill=black)
drawtop.line((14,15,16,15),width=1, fill=black)
drawtop.line((15,14,16,13),width=1, fill=black)
drawtop.line((14,15,13,16),width=1, fill=black)
drawtop.line((10,8,14.5,8),width=1, fill=black)
drawtop.line((10,7,10,9),width=1, fill=black)

##makes imbot
imbot = imtop

imtop.show()
