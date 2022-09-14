from libqtile.lazy import lazy
from qtile_extras.popup.toolkit import (
    PopupRelativeLayout,
    PopupText
)
from libqtile.resources.utils.settings import colors

def bl_applet(qtile):
    controls = [
        PopupText(
            text="Enable",
            pos_x=0.10,
            pos_y=0.1,
            width=0.80,
            height=0.1,
            h_align="center"
        ),
        PopupText(
            text="Disable",
            pos_x=0.10,
            pos_y=0.2,
            width=0.80,
            height=0.1,
            h_align="center"
        ),
        ]

    layout = PopupRelativeLayout(
        qtile,
        width=100,
        height=400,

        controls=controls,
        background=colors["trans"],
        initial_focus=None,
    )

    layout.show(centered=True)
