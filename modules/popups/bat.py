from libqtile.lazy import lazy
from qtile_extras.popup.toolkit import (
    PopupRelativeLayout,
    PopupText
)
from libqtile.resources.utils.settings import colors

import psutil

def bat_applet(qtile):
    bat_stat = psutil.sensors_battery()
    perc = int(bat_stat.percent)
    state = bat_stat.power_plugged
    controls = [
        PopupText(
            text=f"Percent remaining: {perc}",
            pos_x=0.10,
            pos_y=0.1,
            width=0.80,
            height=0.1,
            h_align="left",
            highlight="A00000",
            # mouse_callbacks={
            #     "Button1": lazy.spawn("sudo systemctl start bluetooth")
            # },
        ),
        PopupText(
            text=f"Charging: {state}",
            pos_x=0.10,
            pos_y=0.3,
            width=0.80,
            height=0.1,
            h_align="left",
            highlight="A00000",
            # mouse_callbacks={
            #     "Button1": lazy.spawn("sudo systemctl start bluetooth")
            # },
        ),
        ]

    layout = PopupRelativeLayout(
        qtile,
        width=300,
        height=300,

        controls=controls,
        background=colors["trans"],
        initial_focus=None,
    )

    layout.show(x=0, y=0, relative_to = 3, relative_to_bar=True)
