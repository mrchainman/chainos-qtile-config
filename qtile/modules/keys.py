from libqtile.config import Key
from libqtile.lazy import lazy

# from modules.functions import *
import os
import subprocess

mod = "mod4"
control = "control"
shift = "shift"
alt = "mod1"
terminal = "kitty"
home = os.path.expanduser('~')

# resize functions
def resize(qtile, direction):
    layout = qtile.current_layout
    child = layout.current
    parent = child.parent

    while parent:
        if child in parent.children:
            layout_all = False

            if (direction == "left" and parent.split_horizontal) or (
                direction == "up" and not parent.split_horizontal
            ):
                parent.split_ratio = max(5, parent.split_ratio - layout.grow_amount)
                layout_all = True
            elif (direction == "right" and parent.split_horizontal) or (
                direction == "down" and not parent.split_horizontal
            ):
                parent.split_ratio = min(95, parent.split_ratio + layout.grow_amount)
                layout_all = True

            if layout_all:
                layout.group.layout_all()
                break

        child = parent
        parent = child.parent


@lazy.function
def resize_left(qtile):
    current = qtile.current_layout.name
    layout = qtile.current_layout
    if current == "bsp":
        resize(qtile, "left")
    elif current == "columns":
        layout.cmd_grow_left()


@lazy.function
def resize_right(qtile):
    current = qtile.current_layout.name
    layout = qtile.current_layout
    if current == "bsp":
        resize(qtile, "right")
    elif current == "columns":
        layout.cmd_grow_right()


@lazy.function
def resize_up(qtile):
    current = qtile.current_layout.name
    layout = qtile.current_layout
    if current == "bsp":
        resize(qtile, "up")
    elif current == "columns":
        layout.cmd_grow_up()


@lazy.function
def resize_down(qtile):
    current = qtile.current_layout.name
    layout = qtile.current_layout
    if current == "bsp":
        resize(qtile, "down")
    elif current == "columns":
        layout.cmd_grow_down()


def backlight(action):
    def f(qtile):
        brightness = int(subprocess.run(['brightnessctl', 'g'], stdout=subprocess.PIPE).stdout)
        max_brightness = int(subprocess.run(['brightnessctl', 'm'], stdout=subprocess.PIPE).stdout)
        step = int(max_brightness / 10)

        if action == 'inc':
            if brightness < max_brightness - step:
                subprocess.run(['brightnessctl', 'set', str(brightness + step)], stdout=subprocess.PIPE).stdout
            else:
                subprocess.run(['brightnessctl', 'set', str(max_brightness)], stdout=subprocess.PIPE).stdout
        elif action == 'dec':
            if brightness > step:
                subprocess.run(['brightnessctl', 'set', str(brightness - step)], stdout=subprocess.PIPE).stdout
            else:
                subprocess.run(['brightnessctl', 'set', '0'], stdout=subprocess.PIPE).stdout
    return f


keys = [
    # essentials
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "q", lazy.window.kill(), desc="Kill active window"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle forward layout"),
    Key([mod, shift], "Tab", lazy.prev_layout(), desc="Toggle last layout"),
    # qtile
    Key([mod, shift], "r", lazy.restart(), desc="Restart Qtile"),
    # menus
    Key([mod], "e", lazy.spawn("rofi -show drun -theme ~/.config/rofi/launcher.rasi"), desc="Launch Rofi Launcher"),
    Key([mod], "c", lazy.spawn("rofi -modi 'clipboard:greenclip print' -show clipboard -run-command '{cmd}'"), desc="Launch Rofi Clipboard Manager"),
    Key([mod, shift], "e", lazy.spawn("chainos-toggle_eww"), desc="Launc Eww Power Menu"),
    # focus, move windows and screens
    Key([mod], "j", lazy.layout.down(), desc="Move focus down in current stack pane"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up in current stack pane"),
    Key([mod], "h", lazy.layout.left(), desc="Move focus left in current stack pane"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus right in current stack pane",),
    Key([mod, shift], "j", lazy.layout.shuffle_down(), lazy.layout.move_down(), desc="Move windows down in current stack",),
    Key([mod, shift], "k", lazy.layout.shuffle_up(), lazy.layout.move_up(), desc="Move windows up in current stack",),
    Key([mod, shift], "h", lazy.layout.shuffle_left(), lazy.layout.move_left(), desc="Move windows left in current stack",),
    Key([mod, shift], "l", lazy.layout.shuffle_right(), lazy.layout.move_right(), desc="Move windows right in the current stack",),
    Key([mod], "x", lazy.next_screen(), desc="Move focus to next monitor",),    # TODO find a better hotkey
    Key([mod, control], "j", lazy.layout.flip_down(), desc="Flip layout down"),
    Key([mod, control], "k", lazy.layout.flip_up(), desc="Flip layout up"),
    Key([mod, control], "h", lazy.layout.flip_left(), lazy.layout.swap_column_left(), desc="Flip layout left"),
    Key([mod, control], "l", lazy.layout.flip_right(), lazy.layout.swap_column_left(), desc="Flip layout right"),
    # window resizing
    Key([mod, alt], "h", resize_left, desc="Resize window left"),
    Key([mod, alt], "l", resize_right, desc="Resize window Right"),
    Key([mod, alt], "k", resize_up, desc="Resize windows upward"),
    Key([mod, alt], "j", resize_down, desc="Resize windows downward"),
    Key([mod, alt], "n", lazy.layout.normalize(), desc="Normalize window size ratios"),
    # window states
    Key([mod], "m", lazy.window.toggle_maximize(), desc="Toggle window between minimum and maximum sizes",),
    Key([mod, shift], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod], "i", lazy.window.toggle_floating(), desc="Toggle floating mode for a window"),
    # program launches
    Key([mod], "b", lazy.spawn("chainos-background-switcher new"), desc="Change Wallpaper"),
    Key([mod], "p", lazy.spawn("passmenu"), desc="Launch Passmenu"),
    Key([mod], "f", lazy.spawn("qutebrowser"), desc="Launch Qutebrowser"),
    Key([alt], "e", lazy.spawn("rofi -modi emoji -show emoji"), desc="Launch Rofi Emoji Picker"),
    Key([alt], "l", lazy.spawn("betterlockscreen -l blur"), desc="Lock screen"),
    Key([alt], "p", lazy.spawn("picom-toggle.sh"), desc="Toggle picom"),
    Key([mod], "o", lazy.spawn("opac.sh"), desc="Change opacity of Kitty"),
    Key([mod], "t", lazy.group["scratchpad"].dropdown_toggle("term"), desc="Toggle Scratchpad"),
    # Dunst
    Key([control], "space", lazy.spawn("dunstctl close"), desc="Close last Notification"),
    Key([control, shift], "space", lazy.spawn("dunstctl close-all"), desc="Close all Notifications"),
    Key([control], "grave", lazy.spawn("dunstctl history-pop"), desc="Show old Notifications"),
    Key([control, shift], "period", lazy.spawn("dunstctl context"), desc="Execute Notification context"),
    # Umlaute
    Key([alt], "a", lazy.spawn("umlaute.sh a"), desc="Copy Ä to clipboard"),
    Key([alt], "o", lazy.spawn("umlaute.sh o"), desc="Copy Ö to clipboard"),
    Key([alt], "u", lazy.spawn("umlaute.sh u"), desc="Copy Ü to clipboard"),
    # audio stuff
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pulsemixer --change-volume +10"), desc="Increase volume",),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pulsemixer --change-volume -10"), desc="Decrease volume",),
    Key([], "XF86AudioMute", lazy.spawn("pulsemixer --toggle-mute"), desc="Toggle volume mute",),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Play last audio",),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Play next audio"),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Toggle play/pause audio"),
    # brightness
    Key([], 'XF86MonBrightnessUp', lazy.function(backlight('inc')), desc='Increase brightness'),
    Key([], 'XF86MonBrightnessDown', lazy.function(backlight('dec')), desc='Decrease brightness'),
    # eww
]
