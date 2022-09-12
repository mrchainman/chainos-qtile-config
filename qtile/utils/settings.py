from qtile_extras.widget.decorations import RectDecoration

colors = {
        "base": "#575268",
        "foreground": "#1A1826",
        "accent": "#96CDFB",
        # "accent": "#DDB6F2",
        "highlight": "#F5E0DC",
        "trans": "#00000000",
        "green": "#ABE9B3",
        "maroon": "#E8A2AF",
}

workspace_names = [
"壹",
"贰",
"参",
"肆",
"伍",
"陆",
"柒",
"捌",
"玖",
"拾",
]

def decor():
    return [
        RectDecoration(
            colour=colors["accent"],
            radius=8,
            line_width = 0,
            filled=True,
            padding_x=None,
            padding_y=4,
            group=True,
        )
    ]

# Hardware
network = "bond0"  # network interface name
two_monitors = False # number of screens in the system
with_battery = True  # whether the system uses a battery or not
with_wlan = True   # whether the system uses wlan/internet or not
with_bluetooth = True
