from libqtile.lazy import lazy
from libqtile.backend.x11.window import Window
from qtile_extras.popup.toolkit import (
    PopupText,
    PopupWidget,
    PopupRelativeLayout,
    PopupAbsoluteLayout
)
from libqtile import widget
from datetime import date, datetime
import time
from libqtile.resources.utils.settings import colors

from libqtile.log_utils import logger


class PClock():
    instances = [] 
    def __init__(self,qtile):
        logger.warning(f"Instance count is: {len(self.__class__.instances)}")
        if len(self.__class__.instances) > 0:
            logger.warning("if clause triggered")
            for v in self.__class__.instances:
                v.layout.kill()
                logger.warning(f"Deleted {v}")
                self.__class__.instances = []

        else:
            self.__class__.instances.append(self)
            self.controls = []
            self.controls.append(
                    PopupWidget(
                        widget = widget.Clock(
                            foreground=colors["accent"],
                            format='%H:%M:%S',
                            ),
                        width=200,
                        name = "clock",
                        )
                    )
            # layout = PopupRelativeLayout(
            self.layout = PopupAbsoluteLayout(
                    qtile,
                    width=300,
                    height=50,
                    controls=self.controls,
                    background=colors["trans"],
                    initial_focus=None,
                    )
            self.layout.show(x=0, y=0, relative_to = 3, relative_to_bar=True)
