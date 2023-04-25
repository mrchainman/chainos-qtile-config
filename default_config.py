from libqtile import hook
from libqtile.lazy import lazy
import subprocess
import os

from libqtile.resources.utils.settings import *
from libqtile.resources.utils.presets import *
from libqtile.resources.modules.groups import *
from libqtile.resources.modules.keys import *
from libqtile.resources.modules.layouts import *
from libqtile.resources.modules.screens import *
from libqtile.resources.modules.mouse import *
from libqtile.resources.modules.widgets import *
from libqtile.resources.modules.popups.bl import *
from libqtile.resources.modules.popups.power import *
from libqtile.resources.modules.popups.weather import *
from libqtile.resources.modules.popups.windows import *
from libqtile.resources.modules.hooks import *

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = False
wmname = "qtile"
wl_input_rules = None


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    lazy.group["scratchpad"].dropdown_toggle("mpv")
    subprocess.call([home + "/.config/chainos/qtile_autostart.sh"])
@hook.subscribe.startup
def barclass():
    pass
    # main_screen_bar.window.window.set_property("QTILE_BAR", 1, type="CARDINAL", format=32)
    # second_screen_bar.window.window.set_property("QTILE_BAR", 1, type="CARDINAL", format=32)
    # third_screen_bar.window.window.set_property("QTILE_BAR", 1, type="CARDINAL", format=32)
