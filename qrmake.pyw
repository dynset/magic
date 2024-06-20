import qrcode
import tkinter as tk
from PIL import Image
from PIL import ImageDraw


root = tk.Tk()
root.withdraw()
data = root.clipboard_get()
img_qr = qrcode.make(data)
img_qr.thumbnail((300, 300), resample=Image.BICUBIC)

im_grande = Image.new('RGB', (700, 1200), '#ffffffff')

idraw = ImageDraw.Draw(im_grande)
idraw.text((10, 300), data, fill='#555555')


im_grande.paste(img_qr, (0, 0))
im_grande.save(f'C:\\Users\\arian\\Desktop\\qr_{data[:9]}.png')
root.destroy()
im_grande.show()
