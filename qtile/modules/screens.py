from libqtile import bar
from libqtile.config import Screen

from modules.widgets import *
from utils.settings import colors, two_monitors

widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=15,
    padding=2,
    background=colors["trans"],
    foreground=colors["foreground"],
)
extension_defaults = widget_defaults.copy()


def create_bar(extra_bar = False):
    """Create top bar, defined as function to allow duplication in other monitors"""
    return bar.Bar(
        [
            separator(),
            w_hk,
            separator_bg(),
            *gen_groupbox(),
            gen_spacer(),
            w_window_name_icon,
            separator(),
            w_window_name,
            gen_spacer(),
            w_layout,
            separator(),
            w_flame,
            separator(),
            *w_wlan,
            w_blue,
            *w_battery,
            separator(),
            w_cal,
            w_clock,
            w_wttr,
            separator(),
            w_power,
            separator(),
        ],
        30,
        background=colors["trans"],
        margin=[4, 6, 2, 6],
    )


main_screen_bar = create_bar()
if two_monitors:
    secondary_screen_bar = create_bar(True)
    third_screen_bar = create_bar(True)

screens = [
    Screen(
        # wallpaper=wallpaper_main,
        # wallpaper_mode="fill",
        top=main_screen_bar,
        bottom=bar.Gap(2),
        left=bar.Gap(2),
        right=bar.Gap(2),
    ),
]

if two_monitors:
    screens.append(
        Screen(
            # wallpaper=wallpaper_sec,
            # wallpaper_mode="fill",
            top=secondary_screen_bar,
            bottom=bar.Gap(2),
            left=bar.Gap(2),
            right=bar.Gap(2),
        ),
    )
    screens.append(
        Screen(
            # wallpaper=wallpaper_sec,
            # wallpaper_mode="fill",
            top=third_screen_bar,
            bottom=bar.Gap(2),
            left=bar.Gap(2),
            right=bar.Gap(2),
        ),
    )
