from libqtile import bar
from libqtile.lazy import lazy
from libqtile.log_utils import logger
from qtile_extras import widget
from libqtile.resources.utils.settings import colors, decor, with_wlan, with_battery, with_bluetooth
from libqtile.resources.modules.popups.power import show_power_menu
from libqtile.resources.modules.popups.windows import show_windows_menu
from libqtile.resources.modules.popups.bl import Blue
from libqtile.resources.modules.popups.bat import bat_applet
from libqtile.resources.modules.popups.clock import PClock
#from libqtile.resources.modules.popups.cal_events import Events
from libqtile.resources.modules.popups.randr import Randr
from libqtile.resources.utils.wallpaper import set_random_wallpaper

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
    try:
        status_file = open("/sys/class/power_supply/BAT0/status", "r")
        status = status_file.readline()
    except:
        status = "AC"
    if status == "Discharging\n":
        battery_icon = "/usr/share/icons/BeautyLine/apps/scalable/battery.svg"
    else:
        battery_icon = "/usr/share/icons/BeautyLine/devices/scalable/ac-adapter.svg"
    return battery_icon

def img_widget(func_l=None,func_r=None,spawn=None,scratch=None,x_index=None,img=None):
    mouse_callbacks={}
    if func_l:
        mouse_callbacks["Button1"] = lazy.function(func_l)
    elif scratch:
        lazy.group["scratchpad"].dropdown_toggle(scratch)
    elif spawn:
        mouse_callbacks["Button1"] = lazy.spawn(spawn)

    if func_r:
        mouse_callbacks["Button3"] = lazy.function(func_r, x_index)

    logger.warning(f"{img} has {mouse_callbacks}")
    return(
        separator(),
        widget.Image (
        margin=5,
        mouse_callbacks=mouse_callbacks,
        filename=f"/usr/share/icons/BeautyLine/apps/scalable/{img}.svg",
        decorations=decor(),
        ),
        separator(),
        )

w_pom = (
    separator(),
    widget.Pomodoro(
        length_pomodori=25,
        length_short_break=5,
        num_pomodori=3,
        length_long_break=30,
        decorations=decor(),
        ),
    separator(),
        )


def w_hk(): 
    return img_widget(func_l=set_random_wallpaper, img="python")

def w_layout():   
    return (
        separator(),
        widget.CurrentLayoutIcon(
            padding=8,
            decorations=decor(),
        ),
        separator(),
    )



def w_cal(x_index): 
    return img_widget(func_r=PClock, x_index=x_index, img="calendar")



def w_blue(x_index):
    return img_widget(func_r=Blue, x_index=x_index, scratch="bluetooth",img="bluetooth")

def w_randr(x_index):  
    return img_widget(func_r=Randr, x_index=x_index, scratch="arandr",img="xscreensaver")

def w_flame(x_index): 
    return img_widget(spawn="flameshot gui", x_index=x_index, img="flameshot")

w_bat = (
    separator(),
    widget.Image(
    margin=5,
    mouse_callbacks={
        "Button1": lazy.spawn("kitty"),
        "Button3": lazy.function(bat_applet),
        },
    filename=battery_state(),
    update=battery_state(),
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
