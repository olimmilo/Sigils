from PIL import Image, ImageDraw


width=1000
height=1000

imtop = Image.new("RGB", (width,height), "white")
imbot = Image.new("RGB", (width,height), "white")
immid = Image.new("RGB", (width,height), "white")
drawtop = ImageDraw.Draw(imtop)
drawbot = ImageDraw.Draw(imbot)
drawmid = ImageDraw.Draw(immid)
