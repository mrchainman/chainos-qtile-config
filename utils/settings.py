from qtile_extras.widget.decorations import RectDecoration
from libqtile.resources.utils.presets import *
from Xlib import display
from Xlib.ext import randr
from libqtile.log_utils import logger

colors = sweet
# logger.warning(colors)
colors["trans"] = "#00000000"

# Probably not needed
colors["bat_charging"] = "#ABE9B3"
colors["bat_discharing"] = "#E8A2AF"

workspace_names = chinese

stickys = [
        "chainos-urlhandler",
        "dockx",
        "mpv",
        ]

app_img_maps = {
        "qutebrowser": "web-browser"
        }

terminal = "alacritty"



def decor():
    return [
        RectDecoration(
            colour=colors["accent"],
            radius=8,
            line_width = 0,
            filled=False,
            padding_x=None,
            padding_y=4,
            group=True,
        )
    ]

def get_mon():
    try:
        d = display.Display()
        root = d.screen().root
        monitors = []
        for m in root.xrandr_get_monitors().monitors:
            c = d.get_atom_name(m.name)
            monitors.append(c)
        #logger.warning(f"Monitors: {monitors}\n")
    except:
        monitors = ["None"]
    return monitors

# Hardware
network = "bond0"  # network interface name
monitors = get_mon()
with_battery = True  # whether the system uses a battery or not
with_wlan = True   # whether the system uses wlan/internet or not
with_bluetooth = True
