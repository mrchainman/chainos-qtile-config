from libqtile import bar
from libqtile.config import Screen
import copy

from libqtile.resources.modules.widgets import *
from libqtile.resources.utils.settings import colors, monitors

widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=15,
    padding=2,
    background=colors["trans"],
    foreground=colors["foreground"],
)
extension_defaults = widget_defaults.copy()


def create_bar():
    """Create top bar, defined as function to allow duplication in other monitors"""
    return bar.Bar(
        [
            *w_hk,
            *w_layout(),
            *w_gmenu,
            # gen_spacer(),
            w_notif,
            # *gen_groupbox(),
            gen_spacer(),
            # *w_systray,
            *w_flame,
            *w_blue,
            *w_wifi,
            *w_bat,
            *w_kb,
            *w_cal,
            *w_power,
        ],
        30,
        background=colors["trans"],
        margin=[4, 6, 2, 6],
    )

screens = []

for i in monitors:
    screens.append(
        Screen(
            top=create_bar(),
            bottom=bar.Gap(2),
            left=bar.Gap(2),
            right=bar.Gap(2),
            wallpaper="/home/davidc/.config/wallpaper",
            wallpaper_mode="stretch",
        ),
    )

