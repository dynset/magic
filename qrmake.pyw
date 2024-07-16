from typing import List
import qrcode
import tkinter as tk
from PIL import Image
from PIL import ImageDraw
import utils
from os import sep as SEP

desktop_path = utils.get_desktop_path()
f_format = utils.get_current_time_for_filename()

qr_size = 360

root = tk.Tk()
root.withdraw()
dat = root.clipboard_get()
datas: List[str] = []

if '{' in dat:
    datas.append(dat)
else:
    datas = [x.strip() for x in dat.split('\n')]

for i, data in enumerate(datas):
    img_qr: Image.Image = qrcode.make(data)
    img_qr = img_qr.resize((qr_size, qr_size), resample=Image.BICUBIC)

    cant_lines = len(data.split('\n'))
    max_cant_caracters = max([len(t) for t in data.split('\n')])
    max_cant_caracters = max([36, max_cant_caracters])

    im_grande = Image.new('RGB', (30+10*max_cant_caracters,
                                  20+qr_size+25*cant_lines), '#ffffffff')
    idraw = ImageDraw.Draw(im_grande)

    idraw.text((10, qr_size), data, fill='#555555', font=utils.font_ubuntu)

    im_grande.paste(img_qr, (0, 0))
    im_grande.save(f'{desktop_path}{SEP}qr_{f_format}({i+1}).png')
root.destroy()
