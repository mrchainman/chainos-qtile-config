from libqtile.lazy import lazy
from libqtile.backend.x11.window import Window
from qtile_extras.popup.toolkit import (
    PopupText,
    PopupRelativeLayout
)
from datetime import date, datetime
import time
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
    layout.show(x=0, y=0, relative_to = 3, relative_to_bar=True)
