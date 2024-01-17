import os
import random
from pathlib import Path
from subprocess import Popen


def set_random_wallpaper(qtile):
    home = os.path.expanduser("~")
    wallpapers = os.path.expanduser(f"{home}/.data/Pictures")
    possibles = []
    for img in Path(wallpapers).rglob('*.jpg'):
        possibles.append(img)
    wp = random.choice(possibles)
    os.remove(f"{home}/.config/wallpaper")
    Path(f"{home}/.config/wallpaper").symlink_to(wp)
    qtile.restart() 
    Popen(["betterlockscreen","-u",f"{home}/.config/wallpaper"])
