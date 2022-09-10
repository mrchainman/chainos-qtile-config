from libqtile import bar, qtile, lazy

from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

from utils.settings import colors, with_battery, with_wlan, workspace_names

import os

home = os.path.expanduser("~")

group_box_settings = {
    "active": colors[0],
    "block_highlight_text_color": colors[0],
    "this_current_screen_border": colors[0],
    "this_screen_border": colors[0],
    "urgent_border": colors[3],
    "background": colors[12],  # background is [10-12]
    "other_current_screen_border": colors[12],
    "other_screen_border": colors[12],
    "highlight_color": colors[13],
    "inactive": colors[14],
    "foreground": colors[18],
    "borderwidth": 2,
    "disable_drag": True,
    "fontsize": 14,
    "highlight_method": "line",
    "padding_x": 10,
    "padding_y": 16,
    "rounded": True,
}

# functions for callbacks
def open_launcher():
    qtile.cmd_spawn("rofi -show drun -theme ~/.config/rofi/launcher.rasi")

def open_powermenu():
    qtile.cmd_spawn("power")


def open_calendar():
    qtile.cmd_spawn("toggle_cal")

def open_wifi():
    qtile.cmd_spawn("iwgtk")

def open_flame():
    qtile.cmd_spawn("flameshot gui")

def open_wttr():
    qtile.cmd_spawn("kitty --hold --class='wttr' curl https://wttr.in")

def open_bluetooth():
    qtile.cmd_spawn("blueman-manager")

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
        foreground=colors[12],
        padding=4,
        linewidth=3,
    )


def separator_sm():
    return widget.Sep(
        foreground=colors[12],
        padding=1,
        linewidth=1,
        size_percent=55,
    )


# widget decorations
base_decor = {
    "colour": colors[13],
    "filled": True,
    "padding_y": 4,
    "line_width": 0,
}


def _full_decor(color):
    return [
        RectDecoration(
            colour=color,
            radius=4,
            filled=True,
            padding_y=4,
        )
    ]



def _left_decor(color, padding_x=None, padding_y=4):
    return [
        RectDecoration(
            colour=color,
            radius=4,
            filled=True,
            padding_x=padding_x,
            padding_y=padding_y,
        )
    ]


def _right_decor(color):
    return [
        RectDecoration(
            colour=colors[13],
            radius=4,
            filled=True,
            padding_y=4,
            padding_x=0,
        )
    ]


# hollow knight icon
w_hk = widget.Image(
    margin=5,
    mouse_callbacks={"Button1": open_launcher},
    filename="~/.config/qtile/icons/python.png",
    decorations=_left_decor(colors[8]),
)


# workspace groups
# w_groupbox_1 = widget.GroupBox(  # WEB
#     font="Font Awesome 6 Brands",
#     visible_groups=[workspace_names[0]],
#     **group_box_settings,
# )

# w_groupbox_2 = widget.GroupBox(  # DEV, SYS
#     font="Font Awesome 6 Free Solid",
#     visible_groups=[workspace_names[1], workspace_names[2]],
#     **group_box_settings,
# )

# w_groupbox_3 = widget.GroupBox(  # DISC, MUS
#     font="Font Awesome 6 Brands",
#     visible_groups=[workspace_names[3], workspace_names[4]],
#     **group_box_settings,
# )

# w_groupbox_4 = widget.GroupBox(  # FILE, NOT
#     font="Font Awesome 6 Free Solid",
#     visible_groups=[workspace_names[5], workspace_names[6]],
#     **group_box_settings,
# )


def gen_groupbox():
    return (
        widget.GroupBox(  # WEB
            font="Font Awesome 6 Brands",
            # visible_groups=[workspace_names[0]],
            **group_box_settings,
        ),
        # widget.GroupBox(  # DEV, SYS
        #     font="Font Awesome 6 Free Solid",
        #     visible_groups=[workspace_names[1], workspace_names[2]],
        #     **group_box_settings,
        # ),
        # widget.GroupBox(  # DISC, MUS
        #     font="Font Awesome 6 Brands",
        #     visible_groups=[workspace_names[3], workspace_names[4]],
        #     **group_box_settings,
        # ),
        # widget.GroupBox(  # FILE, NOT
        #     font="Font Awesome 6 Free Solid",
        #     visible_groups=[workspace_names[5], workspace_names[6]],
        #     **group_box_settings,
        # ),
    )


# spacers
def gen_spacer():
    return widget.Spacer()


# window name
w_window_name_icon = widget.TextBox(
    text=" ",
    foreground="#ffffff",
    font="Font Awesome 6 Free Solid",
)

w_window_name = widget.WindowName(
    foreground="#ffffff",
    width=bar.CALCULATED,
    empty_group_string="Desktop",
    max_chars=40,
    parse_text=parse_window_name,
    # mouse_callbacks={"Button1": toggle_maximize},
)


# current layout
def gen_current_layout():
    return (
        widget.CurrentLayoutIcon(
            scale=0.6,
            font="JetBrainsMono Nerd Font",
            fontsize=12,
            padding=8,
            decorations=_left_decor(colors[8]),
        ),
    )


# battery
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
            foreground=colors[11],
            background=colors[12],
            border_colour=colors[11],
            border_charge_colour=colors[11],
            border_critical_colour=colors[11],
            fill_normal=colors[11],
            fill_charge=colors[6],
            fill_critical=colors[2],
            font="JetBrainsMono Nerd Font",
            fontsize=12,
            padding=8,
            decorations=_left_decor(colors[8]),
        ),
    )
    # if with_battery
    # else ()
)


# internet
w_wlan = (
        widget.WiFiIcon(
            active_colour=colors[11],
            inactive_colour=colors[16],
            background=colors[12],
            foreground=colors[11],
            font="Font Awesome 6 Free Solid:style=Solid",
            fontsize=16,
            interface="wlan0",
            update_interval=5,
            mouse_callbacks={"Button3": open_wifi},
            padding=8,
            decorations=_left_decor(colors[8]),
        ),
)

# time, calendar
def gen_clock():
    color = colors[8]

    return (
        widget.TextBox(
            text="",
            font="JetBrainsMono Nerd Font",
            fontsize=16,
            foreground=colors[10],  # blue
            padding=8,
            decorations=_left_decor(color),
            mouse_callbacks={"Button1": open_calendar},
        ),
    )

w_flame = (
    widget.TextBox(
        text="",
        font="Font Awesome 6 Free Solid:style=Solid",
        foreground=colors[10],  # blue
        fontsize=30,
        padding=8,
        decorations=_left_decor(colors[8]),
        mouse_callbacks={"Button1": open_flame},
        )
)

w_wttr = (
        widget.Wttr(
            location = { 'Berlin': 'Berlin' },
            font="JetBrainsMono Nerd Font",
            fontsize=16,
            foreground=colors[10],  # blue
            padding=8,
            decorations=_left_decor(colors[8]),
            mouse_callbacks={"Button1": open_wttr},
        )
)

w_blue = (
        widget.Bluetooth(
            fmt=" {}",
            hci="/dev_E1_4A_BB_C7_62_0F",
            foreground=colors[11],
            font="Font Awesome 6 Free Solid:style=Solid",
            fontsize=16,
            padding=16,
            decorations=_left_decor(colors[8]),
            mouse_callbacks={"Button1": open_bluetooth},
            )
        )

w_power = widget.TextBox(
    text="⏻",
    foreground=colors[11],
    font="Font Awesome 6 Free Solid:style=Solid",
    fontsize=18,
    padding=16,
    decorations=_left_decor(colors[8]),
    mouse_callbacks={"Button1": open_powermenu},
)
