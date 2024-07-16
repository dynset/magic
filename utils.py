from datetime import datetime
import os
from PIL import ImageFont


def get_desktop_path():
    desktop_eng = os.path.expanduser("~/Desktop")
    if os.path.exists(desktop_eng):
        return desktop_eng
    return os.path.expanduser("~/Escritorio")  # asumming spanish


def get_current_time_for_filename():
    """@returns [d] m_s(i)"""
    f = datetime.today()
    return f'{f.day}_{f.hour}_{f.minute}_{f.second}'


font_ubuntu = ImageFont.truetype('ubuntu-ligth.ttf', size=22)
