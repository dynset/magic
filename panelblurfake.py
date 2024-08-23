from PIL import Image, ImageFilter

#Open existing image
ori = Image.open('d.jpg')
sx,sy=ori.size
print(sx,sy)
corte_y=sy-110
panel=ori.crop((0,corte_y,sx,sy))
#panel.show()
gaussImage = panel.filter(ImageFilter.GaussianBlur(18))
ori.paste(gaussImage,(0,corte_y))
ori.show()
