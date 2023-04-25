from libqtile.lazy import lazy
from libqtile.backend.x11.window import Window
from qtile_extras.popup.toolkit import (
    PopupText,
    PopupWidget,
    PopupGridLayout,
)
from libqtile import widget
from datetime import date, datetime
import time
from libqtile.resources.utils.settings import colors

from libqtile.log_utils import logger
import calendar


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
            self.cal = calendar.Calendar()
            self.month = date.today().month
            self.gen_all()
            self.gen_layout(qtile)
            self.show_layout()

    def gen_all(self):
        self.controls = []
        self.gen_clock_gui()
        self.gen_month_switcher()
        self.gen_calendar_gui()

    def show_layout(self):
        self.layout.show(x=0, y=0, relative_to = 3, relative_to_bar=True)

    def gen_layout(self,qtile):
        self.layout = PopupGridLayout(
                            qtile,
                            rows=7,
                            cols=7,
                            width=400,
                            height=300,
                            controls=self.controls,
                            background=colors["trans"],
                            initial_focus=None,
                            close_on_click=False,
                            )

    def gen_clock_gui(self):
        self.controls.append(
                        PopupWidget(
                            widget = widget.Clock(
                                foreground=colors["accent"],
                                format='%H:%M:%S',
                                ),
                            # width=100,
                            col=3,
                            row=0,
                            col_span=3,
                            name = "clock",
                            )
                        )

    def gen_calendar(self):
        days = []
        today = date.today()
        i = self.cal.itermonthdays2(today.year,self.month)
        for m,k in i:
            if m != 0:
                if k == 0:
                    d = "Mo"
                if k == 1:
                    d = "Tu"
                if k == 2:
                    d = "We"
                if k == 3:
                    d = "Th"
                if k == 4:
                    d = "Fr"
                if k == 5:
                    d = "Sa"
                if k == 6:
                    d = "Su"
                days.append((m,d))
        return today, days

    def gen_calendar_gui(self):
        today, days = self.gen_calendar()
        ri = 2
        ci = 0
        for i,j in days:
            if i == int(today.strftime("%d")):
                bg = colors["accent"]
            else:
                bg = colors["trans"]
            self.controls.append(
                    PopupText(
                        name=f"{str(i)}-day",
                        text=str(j+"\n"+str(i)),
                        row = ri,
                        col = ci,
                        width=0.1,
                        height=0.1,
                        h_align="center",
                        highlight=colors["accent"],
                        highlight_method="block",
                        background=bg,
                        can_focus=True,
                        mouse_callbacks={
                            # "Button1": qtile.cmd_spawn(f"kitty khal at {i}/{today.month}/{today.year}"),
                        },
                        )
                    )
            if ci < 6:
                ci += 1
            else:
                ri += 1
                ci = 0

    def gen_month_switcher(self):
        self.controls.append(
                    PopupText(
                        text="<",
                        row = 1,
                        col = 0,
                        col_span = 3,
                        h_align="center",
                        highlight=colors["accent"],
                        highlight_method="block",
                        background=colors["trans"],
                        can_focus=True,
                        mouse_callbacks={
                            "Button1": self.month_back,
                        },
                        )
                )

    def month_back(self):
        self.month -= 1
        logger.warning(f"Set month to {self.month}")
        self.gen_all()
        self.show_layout()
        



