from datetime import datetime
import os
from PIL import ImageFont


def get_desktop_path():
    return os.path.expanduser("~/Desktop")


def get_current_time_for_filename():
    f = datetime.today()
    return f'[{f.day}] {f.hour}_{f.minute}_{f.second}'


font_ubuntu = ImageFont.truetype('ubuntu-ligth.ttf', size=22)
