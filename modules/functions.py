from libqtile import qtile
from libqtile import hook
from libqtile.lazy import lazy
import os
home = os.path.expanduser("~")

def open_launcher():
    qtile.spawn("rofi -show drun -theme ~/.config/rofi/launcher.rasi")

def open_calendar():
    pass

def open_wifi():
    qtile.spawn("iwgtk")

def open_flame():
    qtile.spawn("flameshot gui")

def open_wttr():
    qtile.spawn("kitty --hold --class='wttr' curl https://wttr.in")

def open_bluetooth():
    qtile.spawn("blueman-manager")



