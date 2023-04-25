from libqtile import bar
from libqtile.lazy import lazy
from libqtile.log_utils import logger
from qtile_extras import widget
from libqtile.resources.utils.settings import colors, decor, with_wlan, with_battery, with_bluetooth
from libqtile.resources.modules.popups.power import show_power_menu
from libqtile.resources.modules.popups.windows import show_windows_menu
from libqtile.resources.modules.popups.bl import bl_applet
from libqtile.resources.modules.popups.bat import bat_applet
from libqtile.resources.modules.popups.calendar import gen_gui
from libqtile.resources.modules.popups.clock import PClock

import os

home = os.path.expanduser("~")

group_box_settings = {
    "active": colors["accent"],
    "inactive": colors["accent2"],
    "block_highlight_text_color": colors["base"],
    "highlight_color": colors["trans"],
    "disable_drag": True,
    "highlight_method": "line",
    "padding_x": 10,
    "padding_y": 16,
    "hide_unused": True,
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

def battery_state():
    status_file = open("/sys/class/power_supply/BAT0/status", "r")
    status = status_file.readline()
    if status == "Discharging\n":
        battery_icon = "/usr/share/icons/BeautyLine/apps/scalable/battery.svg"
    else:
        battery_icon = "/usr/share/icons/BeautyLine/devices/scalable/ac-adapter.svg"
    return battery_icon


w_hk = (
    separator(),
    widget.Image (
    margin=5,
    mouse_callbacks={"Button1": lazy.function(show_windows_menu)},
    filename="/usr/share/icons/BeautyLine/apps/scalable/python.svg",
    decorations=decor(),
    ),
    separator(),
)


# w_layout =  (
#     separator(),
#     widget.CurrentLayout(
#         padding=8,
#         decorations=decor(),
#     ),
#     separator(),
# )

def w_layout():   
    return (
        separator(),
        widget.CurrentLayoutIcon(
            padding=8,
            decorations=decor(),
        ),
        separator(),
    )



 # w_notif = (
 #        widget.Notify(
 #       #     decorations=decor(),
 #            )
 #        )

w_cal = (
    separator(),
    widget.Image(
        margin=5,
        mouse_callbacks={
            "Button1": lazy.function(PClock),
            "Button3": lazy.function(gen_gui),
            },
        filename="/usr/share/icons/BeautyLine/apps/scalable/calendar.svg",
        decorations=decor(),
    ),
    separator(),
)


w_flame = (
    # separator(),
    widget.Image(
        margin=5,
        mouse_callbacks={"Button1": lazy.spawn("flameshot gui")},
        filename="/usr/share/icons/BeautyLine/apps/scalable/flameshot.svg",
        decorations=decor(),
    ),
    separator(),
)



w_blue = (
    separator(),
    widget.Image(
    margin=5,
    mouse_callbacks={
        "Button1": lazy.group["scratchpad"].dropdown_toggle("bluetooth"),
        "Button3": lazy.function(bl_applet),
    },
    filename="/usr/share/icons/BeautyLine/apps/scalable/bluetooth.svg",
    decorations=decor(),
    ),
    separator(),
)

w_bat = (
    separator(),
    widget.Image(
    margin=5,
    mouse_callbacks={
        "Button1": lazy.spawn("kitty"),
        "Button3": lazy.function(bat_applet),
        },
    filename=battery_state(),
    decorations=decor(),
    ),
    separator(),
)

w_wifi = (
    separator(),
    widget.Image(
    margin=5,
    mouse_callbacks={
        "Button1": lazy.group["scratchpad"].dropdown_toggle("wifi"),
        # "Button1": lazy.spawn("iwgtk")
        },
    filename="/usr/share/icons/BeautyLine/apps/scalable/wifi-radar.svg",
    decorations=decor(),
    ),
    separator(),
)

w_kb = (
    separator(),
    widget.Image(
    margin=5,
    mouse_callbacks={"Button1": lazy.spawn("chainos-kb-layout")},
    filename="/usr/share/icons/BeautyLine/actions/scalable/help-keybord-shortcuts.svg",
    decorations=decor(),
    ),
    separator(),
)

w_power = (
    separator(),
    widget.Image(
        margin=5,
        mouse_callbacks={"Button1": lazy.function(show_power_menu)},
        filename="/usr/share/icons/BeautyLine/actions/scalable/system-shutdown.svg",
        decorations=decor(),
    ),
    separator(),
)

w_systray = (
    separator(),
    widget.StatusNotifier(
        margin=5,
        icon_theme="BeautyLine",
        decorations=decor(),
        icon_size=20,
        menu_background=colors["trans"],
        # menu_foreground=colors["foreground"],
        menu_foreground="#FFFFFF",
        padding=33,
        ),
    # separator(),
    )

w_gmenu = (
    separator(),
    widget.GlobalMenu(
        margin=5,
        decorations=decor(),
        menu_background=colors["trans"],
        # menu_foreground=colors["foreground"],
        menu_foreground="#FFFFFF",
        padding=33,
        ),
    separator(),
        )


# w_clock = (
#     widget.Clock(
#         padding=8,
#         decorations=decor(),
#         )
# )


# w_blue = (
#         widget.Bluetooth(
#             fmt="{}",
#             hci="/dev_E1_4A_BB_C7_62_0F",
#             padding=16,
#             decorations=decor(),
#             mouse_callbacks={"Button1": lazy.spawn("kitty bluetuith"), "Button3": lazy.function(bl_applet)},
#             )
#         )


# w_wttr = (
#         widget.Wttr(
#             location = { 'Berlin': 'Berlin' },
#             padding=8,
#             decorations=decor(),
#             mouse_callbacks={"Button1": lazy.spawn("kitty --hold curl https://wttr.in")},
#         )
# )


# internet
# w_wlan = (
#     separator(),
#     widget.WiFiIcon(
#         active_colour=colors["foreground"],
#         inactive_colour=colors["base"],
#         interface="wlan0",
#         update_interval=5,
#         mouse_callbacks={"Button1": lazy.spawn("iwgtk")},
#         padding=8,
#         decorations=decor(),
#     ),
#     separator(),
# )


# # battery
# w_battery = (
#     separator(),
#     widget.UPowerWidget(
#         format="{char}",
#         charge_char="",
#         discharge_char="",
#         full_char="",
#         unknown_char="",
#         empty_char="",
#         show_short_text=False,
#         border_colour=colors["foreground"],
#         border_charge_colour=colors["foreground"],
#         border_critical_colour=colors["foreground"],
#         fill_normal=colors["foreground"],
#         fill_charge=colors["bat_charging"],
#         fill_critical=colors["bat_discharing"],
#         padding=8,
#         decorations=decor(),
#     ),
#     separator(),
# )
