from libqtile.lazy import lazy
from libqtile.backend.x11.window import Window
from qtile_extras.popup.toolkit import (
    PopupText,
    PopupRelativeLayout
)
from datetime import date, datetime
from libqtile.resources.utils.settings import colors


def gen_clock(qtile):
    controls = []
    cur_time = datetime.now().strftime("%H:%M:%S")
    controls.append(
            PopupText(
                 text=str(cur_time),
                 width=1,
                 height=1,
                 h_align="center",
                 highlight=colors["accent"],
                 highlight_method="block",
                 background=colors["trans"],               
                )
            )
    layout = PopupRelativeLayout(
            qtile,
            width=300,
            height=50,
            controls=controls,
            background=colors["trans"],
            initial_focus=None,
            )
    layout.show(pos_x=10, pos_y=1000)
