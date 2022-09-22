from qtile_extras.widget.decorations import RectDecoration
from libqtile.resources.utils.presets import *

theme = mocca

colors = {
        "base": theme["base"],
        "foreground": theme["base"],
        "accent": theme["blue"],
        "accent2": theme["mauve"],
        "highlight": theme["yellow"],
        "trans": "#00000000",
        "bat_charging": "#ABE9B3",
        "bat_discharing": "#E8A2AF",
}

workspace_names = chinese


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

# Hardware
network = "bond0"  # network interface name
two_monitors = True # number of screens in the system
with_battery = True  # whether the system uses a battery or not
with_wlan = True   # whether the system uses wlan/internet or not
with_bluetooth = True
