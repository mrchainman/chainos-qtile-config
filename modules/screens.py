from libqtile import bar
from libqtile.config import Screen

from libqtile.resources.modules.widgets import *
from libqtile.resources.utils.settings import colors, two_monitors

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
            *w_hk,
            gen_spacer(),
            *gen_groupbox(),
            gen_spacer(),
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


main_screen_bar = create_bar()
if two_monitors:
    secondary_screen_bar = create_bar(True)
    third_screen_bar = create_bar(True)

screens = [
    Screen(
        top=main_screen_bar,
        bottom=bar.Gap(2),
        left=bar.Gap(2),
        right=bar.Gap(2),
    ),
]

if two_monitors:
    screens.append(
        Screen(
            top=secondary_screen_bar,
            bottom=bar.Gap(2),
            left=bar.Gap(2),
            right=bar.Gap(2),
        ),
    )
    screens.append(
        Screen(
            top=third_screen_bar,
            bottom=bar.Gap(2),
            left=bar.Gap(2),
            right=bar.Gap(2),
        ),
    )
