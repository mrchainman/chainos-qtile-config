from libqtile.lazy import lazy
from qtile_extras.popup.toolkit import (
    PopupGridLayout,
    PopupText
)
from libqtile.resources.utils.settings import colors
import os

from libqtile.resources.modules.popups.baseclass import Base

class Randr(Base):
    def __init__(self,qtile,x_index=0):
        super().__init__(qtile,x_index)


    def _startup(self):
        self.rowcount = 0
        self.randr_applet()
        self.gen_layout(
                self.qtile_instance,
                rows=self.rowcount,
                cols=1,
                width=100,
                height=len(self.controls*40)
                )
        self.show_layout()

    def randr_applet(self):
        ri = 0
        for mode in os.listdir(os.path.expanduser("~/.config/autorandr")):
            self.controls.append(
            PopupText(
                text=mode,
                row = ri,
                col = 0,
                h_align="center",
                highlight=colors["accent"],
                highlight_method="block",
                mouse_callbacks={
                    "Button1": lazy.spawn(f"autorandr --load {mode}")
                },
            )
            )
            ri += 1
        self.rowcount = ri + 1

