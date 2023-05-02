from libqtile.lazy import lazy
from qtile_extras.popup.toolkit import (
    PopupGridLayout,
    PopupText
)
from libqtile.resources.utils.settings import colors

def bl_applet(qtile,x_index):
    controls = [
        PopupText(
            text="Enable",
            row = 0,
            col = 0,
            h_align="center",
            highlight=colors["accent"],
            highlight_method="block",
            mouse_callbacks={
                "Button1": lazy.spawn("sudo systemctl start bluetooth")
            },
        ),
        PopupText(
            text="Disable",
            row = 1,
            col = 0,
            h_align="center",
            highlight=colors["accent"],
            highlight_method="block",
            mouse_callbacks={
                "Button1": lazy.spawn("sudo systemctl stop bluetooth")
            },
        ),
        ]


    layout = PopupGridLayout(
        qtile,

        width=100,
        height = len(controls) * 80,

        cols = 1,
        rows = 5,


        controls=controls,
        background=colors["trans"],
        initial_focus=None,
    )

    layout.show(x=x_index, y=0, relative_to = 3, relative_to_bar=True)
