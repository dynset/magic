from PIL import ImageGrab
from datetime import datetime
import tkinter as tk

img = ImageGrab.grabclipboard()
if img is not None:
    f = datetime.today()
    f_format = f'[{f.day}]{f.hour}-{f.minute}-{f.second}'
    try:
        img.save(f'C:\\Users\\arian\\Desktop\\zzci_{f_format}.png')
    except Exception as e:
        root = tk.Tk()
        root.title('guardador d clipboard')
        lab = tk.Label(root)
        lab['text'] = f'Error: {e}'
        lab.pack(padx=80, pady=40)
        root.mainloop()
else:
    print('no coji nada del clipboard')
    root = tk.Tk()
    root.title('guardador d clipboard')
    lab = tk.Label(root)
    lab['text'] = 'No habia nada en el clipboard..'
    lab.pack(padx=80, pady=40)
    root.mainloop()
