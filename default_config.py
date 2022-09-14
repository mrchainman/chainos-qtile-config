from libqtile import hook
import subprocess
import os

from libqtile.resources.modules.groups import groups
from libqtile.resources.modules.keys import keys, mod, shift
from libqtile.resources.modules.layouts import layouts, floating_layout
from libqtile.resources.modules.screens import screens, main_screen_bar, widget_defaults

# TODOs
# - customize special rofi menus - DONE (room for improvement)
# - qtile hooks
mouse = []
# REVIEW options
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

# # TODO take a look at hooks
# # @hook.subscribe.startup
# # def start():
# #     main_screen_bar.window.window.set_property("QTILE_BAR", 1)

# @hook.subscribe.startup_once
# def start_once():
#     home = os.path.expanduser("~")
#     subprocess.call([home + ".config/chainos/qtile_autostart.sh"])
