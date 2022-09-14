from libqtile import bar
from libqtile.lazy import lazy
from qtile_extras import widget
from libqtile.resources.utils.settings import colors, decor, with_wlan, with_battery, with_bluetooth
from libqtile.resources.modules.functions import open_launcher, open_calendar, open_wifi, open_flame, open_wttr, open_bluetooth
from libqtile.resources.modules.popups.power import show_power_menu
from libqtile.resources.modules.popups.windows import show_windows_menu
from libqtile.resources.modules.popups.bl import bl_applet
from libqtile.resources.modules.popups.calendar import gen_gui

import os

home = os.path.expanduser("~")

group_box_settings = {
    "active": colors["foreground"],
    "inactive": colors["base"],
    "block_highlight_text_color": colors["highlight"],
    "highlight_color": colors["trans"],
    "disable_drag": True,
    "highlight_method": "line",
    "padding_x": 10,
    "padding_y": 16,
}

# TODO fix
# def toggle_maximize():
#     lazy.window.toggle_maximize()


def parse_window_name(text):
    """Simplifies the names of a few windows, to be displayed in the bar"""
    target_names = [
        "Mozilla Firefox",
        "Visual Studio Code",
        "Discord",
    ]
    return next(filter(lambda name: name in text, target_names), text)


# separator
def separator():
    return widget.Sep(
        foreground=colors["trans"],
        padding=4,
        linewidth=3,
    )

def separator_bg():
    return widget.Sep(
        foreground=colors["trans"],
        padding=4,
        linewidth=40,
    )

def separator_sm():
    return widget.Sep(
        foreground=colors["trans"],
        padding=1,
        linewidth=1,
        size_percent=55,
    )


# widget decorations

# hollow knight icon
w_hk = widget.Image(
    margin=5,
    mouse_callbacks={"Button1": open_launcher},
    filename="/usr/share/icons/chainos/python.png",
    decorations=decor(),
)


def gen_groupbox():
    return (
        widget.GroupBox(  # WEB
            **group_box_settings,
            decorations=decor(),
        ),
    )


# spacers
def gen_spacer():
    return widget.Spacer()


# window name
w_window_name_icon = widget.TextBox(
    text=" ",
    background=colors["trans"],
    foreground=colors["foreground"],
)

w_window_name = widget.WindowName(
    background=colors["trans"],
    width=bar.CALCULATED,
    empty_group_string="Desktop",
    max_chars=40,
    parse_text=parse_window_name,
    foreground=colors["foreground"],
    mouse_callbacks={"Button1": lazy.function(show_windows_menu)},
)


# current layout
w_layout =  widget.CurrentLayout(
            padding=8,
            decorations=decor(),
        )


# battery
if with_battery:
    w_battery = (
        (
            widget.UPowerWidget(
                format="{char}",
                charge_char="",
                discharge_char="",
                full_char="",
                unknown_char="",
                empty_char="",
                show_short_text=False,
                border_colour=colors["foreground"],
                border_charge_colour=colors["foreground"],
                border_critical_colour=colors["foreground"],
                fill_normal=colors["foreground"],
                fill_charge=colors["bat_charging"],
                fill_critical=colors["bat_discharing"],
                padding=8,
                decorations=decor(),
            ),
        )
    )
else:
    w_battery = ""

# internet
if with_wlan:
    w_wlan = (
            widget.WiFiIcon(
                active_colour=colors["foreground"],
                inactive_colour=colors["base"],
                interface="wlan0",
                update_interval=5,
                mouse_callbacks={"Button1": open_wifi},
                padding=8,
                decorations=decor(),
            ),
    )
else:
    w_wlan = ""

# time, calendar
w_cal = (
            widget.TextBox(
            text="  ",
            padding=8,
            decorations=decor(),
            mouse_callbacks={"Button1": lazy.function(gen_gui)},
    )
)

w_clock = (
    widget.Clock(
        padding=8,
        decorations=decor(),
        )
)

w_flame = (
    widget.TextBox(
        text="   ",
        padding=8,
        decorations=decor(),
        mouse_callbacks={"Button1": open_flame},
        )
)

w_wttr = (
        widget.Wttr(
            location = { 'Berlin': 'Berlin' },
            padding=8,
            decorations=decor(),
            mouse_callbacks={"Button1": open_wttr},
        )
)

if with_bluetooth:
    w_blue = (
            widget.Bluetooth(
                fmt=" {}",
                hci="/dev_E1_4A_BB_C7_62_0F",
                padding=16,
                decorations=decor(),
                mouse_callbacks={"Button1": open_bluetooth, "Button3": lazy.function(bl_applet)},
                )
            )
else:
    w_blue = ""

w_power = widget.TextBox(
    text=" ⏻ ",
    padding=16,
    decorations=decor(),
    mouse_callbacks={"Button1": lazy.function(show_power_menu)},
)
