from libqtile.lazy import lazy
from qtile_extras.popup.toolkit import (
    PopupGridLayout,
    PopupText
)
from libqtile.resources.utils.settings import colors


from libqtile.resources.modules.popups.baseclass import Base

class Blue(Base):
    def __init__(self,qtile,x_index=0):
        super().__init__(qtile,x_index)

    def _startup(self):

        self.rowcount = 5
        self.bl_applet()
        self.gen_layout(
                self.qtile_instance,
                rows=self.rowcount,
                cols=1,
                width=100,
                height=len(self.controls*80)
                )
        self.show_layout()

    def bl_applet(self):
        self.controls = [
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
