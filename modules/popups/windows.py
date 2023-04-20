from libqtile.lazy import lazy
from libqtile.backend.x11.window import Window
from qtile_extras.popup.toolkit import (
    PopupGridLayout,
    PopupText
)
import os
from libqtile.resources.utils.settings import colors
# from libqtile.log_utils import logger

def wrapperstuff(win):
    group = win.group
    name = win.name
    group.toscreen()
    group.focus_by_name(name)

def show_windows_menu(qtile):
    controls = []
    ri = 0
    ci = 0
    for i in qtile.windows_map.values():
        if isinstance(i, Window):
            controls.append(
                    PopupText(
                        text=str(i.name),
                        row = ri,
                        col = ci,
                        width=0.1,
                        height=1,
                        h_align="center",
                        highlight=colors["accent"],
                        highlight_method="block",
                        background=colors["trans"],
                        can_focus=True,
                        mouse_callbacks={
                            "Button1": lambda value=i: wrapperstuff(value),
                        },
                        )
                    )
            if ci < 4:
                ci += 1
            else:
                ri += 1
                ci = 0

    layout = PopupGridLayout(
        qtile,
        rows=10,
        cols=5,
        width=1000,
        height=500,
        controls=controls,
        background=colors["trans"],
        initial_focus=None,
    )

    layout.show(centered=True)
