from libqtile.lazy import lazy
from qtile_extras.popup.toolkit import (
    PopupGridLayout,
    PopupText
)
from libqtile.resources.utils.settings import colors
import os

def randr_applet(qtile):
    controls = [ ]

    ri = 0
    for mode in os.listdir(os.path.expanduser("~/.config/autorandr")):
        controls.append(
        PopupText(
            text=mode,
            row = ri,
            col = 0,
            width=0.80,
            height=0.1,
            h_align="center",
            highlight=colors["accent"],
            highlight_method="block",
            mouse_callbacks={
                "Button1": lazy.spawn(f"autorandr --load {mode}")
            },
        )
        )
        ri += 1

    layout = PopupGridLayout(
        qtile,
        width=300,
        height=300,

        controls=controls,
        background=colors["trans"],
        initial_focus=None,
    )

    layout.show(x=0, y=0, relative_to = 3, relative_to_bar=True)
