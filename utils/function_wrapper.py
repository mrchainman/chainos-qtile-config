#!/usr/bin/python
from libqtile.lazy import lazy


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
    elif current == "tile":
        layout.cmd_decrease_ratio()


@lazy.function
def resize_right(qtile):
    current = qtile.current_layout.name
    layout = qtile.current_layout
    if current == "bsp":
        resize(qtile, "right")
    elif current == "columns":
        layout.cmd_grow_right()
    elif current == "tile":
        layout.cmd_increase_ratio()


@lazy.function
def resize_up(qtile):
    current = qtile.current_layout.name
    layout = qtile.current_layout
    if current == "bsp":
        resize(qtile, "up")
    elif current == "columns":
        layout.cmd_grow_up()
    elif current == "tile":
        layout.cmd_increase_nmaster()

@lazy.function
def resize_down(qtile):
    current = qtile.current_layout.name
    layout = qtile.current_layout
    if current == "bsp":
        resize(qtile, "down")
    elif current == "columns":
        layout.cmd_grow_down()
    elif current == "tile":
        layout.cmd_decrease_nmaster()


@lazy.function
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

@lazy.function
def go_up(qtile):
    layout = qtile.current_layout
    layout.up()

@lazy.function
def go_down(qtile):
    layout = qtile.current_layout
    layout.down()

@lazy.function
def go_left(qtile):
    layout = qtile.current_layout
    layout.left()

@lazy.function
def go_right(qtile):
    layout = qtile.current_layout
    layout.right()

@lazy.function
def move_up(qtile):
    layout = qtile.current_layout
    layout.shuffle_up()
    layout.move_up()

@lazy.function
def move_down(qtile):
    layout = qtile.current_layout
    layout.shuffle_down()
    layout.move_down()

@lazy.function
def move_left(qtile):
    layout = qtile.current_layout
    layout.shuffle_left()
    layout.move_left()

@lazy.function
def move_right(qtile):
    layout = qtile.current_layout
    layout.shuffle_right()
    layout.move_right()

@lazy.function
def flip_up(qtile):
    layout = qtile.current_layout
    layout.flip_up()

@lazy.function
def flip_down(qtile):
    layout = qtile.current_layout
    layout.flip_down()

@lazy.function
def flip_left(qtile):
    layout = qtile.current_layout
    layout.flip_left()
    layout.swap_column_left()

@lazy.function
def flip_right(qtile):
    layout = qtile.current_layout
    layout.flip_right()
    layout.swap_column_right()
