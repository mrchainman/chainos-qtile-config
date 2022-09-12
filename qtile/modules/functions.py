from libqtile import qtile
import os
home = os.path.expanduser("~")

def open_launcher():
    qtile.cmd_spawn("rofi -show drun -theme ~/.config/rofi/launcher.rasi")

def open_calendar():
    qtile.cmd_spawn("chainos-toggle_cal")

def open_wifi():
    qtile.cmd_spawn("iwgtk")

def open_flame():
    qtile.cmd_spawn("flameshot gui")

def open_wttr():
    qtile.cmd_spawn("kitty --hold --class='wttr' curl https://wttr.in")

def open_bluetooth():
    qtile.cmd_spawn("blueman-manager")
