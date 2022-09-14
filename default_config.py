from libqtile import hook
import subprocess
import os

from libqtile.resources.modules.groups import groups
from libqtile.resources.modules.keys import keys
from libqtile.resources.modules.layouts import layouts
from libqtile.resources.modules.screens import screens
from libqtile.resources.modules.mouse import mouse
from libqtile.resources.modules.widgets import extension_defaults,widget_defaults

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
wl_input_rules = {}

# TODO take a look at hooks
# @hook.subscribe.startup
# def start():
#     main_screen_bar.window.window.set_property("QTILE_BAR", 1)
 # Really we'd want to check this Any is libqtile.backend.wayland.ImportConfig, but
 # doing so forces the import, creating a hard dependency for wlroots.
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/chainos/qtile_autostart.sh"])
