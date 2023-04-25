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


class mday():
    def __init__(self, name, monthday, weekday, isthismonth=True, istoday=False):
        self.name = name
        self.monthday = monthday
        self.weekday = weekday
        self.istoday = istoday
        self.isthismonth = isthismonth

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
            self.days = []
            self.gen_all()
            self.gen_layout(qtile)
            self.show_layout()

    def gen_all(self):
        self.controls = []
        self.gen_clock_gui()
        self.gen_calendar()
        self.gen_calendar_gui()
        self.gen_month_switcher()

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
        self.days = []
        today = date.today().strftime("%d")
        year = date.today().year
        i = self.cal.monthdays2calendar(year,self.month)
        counter = 0
        for week in i:
            for m,k in week:
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
                self.days.append(
                        mday(name=f"slot_{counter}",monthday=m,weekday=d,isthismonth= True if m > 0 else False, istoday= True if m == today else False)
                        )
                counter += 1
        

    def gen_calendar_gui(self):
        ri = 2
        ci = 0
        for i in self.days:
            if i.istoday == True:
                bg = colors["accent"]
            else:
                bg = colors["trans"]
            self.controls.append(
                    PopupText(
                        name= i.name,
                        text=f"{i.weekday}\n{i.monthday}",
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
        if self.month > 0:
            logger.warning("month is above 0")
            self.month -= 1
            self.gen_calendar()
            logger.warning("regenerated calendar")
            for i in self.days:
                if i.name in self.layout._updateable_controls:
                    self.layout._updateable_controls[i.name] = f"{self.days[0].weekday}\n{self.days[0].monthday}"
                else:
                    logger.warning(f"Could not update control {i.name}")
            self.layout.draw()
            logger.warning("redrew popup")
        else:
            logger.warning(f"Can not go below {self.month}")
