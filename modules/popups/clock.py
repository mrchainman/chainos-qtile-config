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
from libqtile.resources.modules.popups.baseclass import Base

from libqtile.log_utils import logger
import calendar




import sys
import datetime
import time
import os
sys.path.append(os.path.expanduser("~/.data/Development/ChainOS/chainos-packages/python-libs/chainos_python_libs/work/"))
#import office365


class mday():
    def __init__(self, name, monthday, weekday, isthismonth=True, istoday=False):
        self.name = name
        self.monthday = monthday
        self.weekday = weekday
        self.istoday = istoday
        self.isthismonth = isthismonth

class PClock(Base):
    def __init__(self,qtile,x_index=0):
        super().__init__(qtile,x_index)

    def _startup(self):
        self.cal = calendar.Calendar()
        self.month = date.today().month
        self.days = []
        self.gen_all()
        self.gen_layout(self.qtile_instance,rows=7,cols=7,width=400,height=300)
        self.show_layout()

    def gen_all(self):
        self.controls = []
        self.gen_clock_gui()
        self.gen_calendar()
        self.gen_calendar_gui()
        self.gen_month_switcher()






    def gen_clock_gui(self):
        self.controls.append(
                        PopupWidget(
                            widget = widget.Clock(
                                foreground="#ffffff",
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
                        mday(name=f"slot_{counter}",monthday=m,weekday=d,isthismonth= True if m > 0 else False, istoday= True if m == int(today) else False)
                        )
                counter += 1
        

    def gen_calendar_gui(self):
        ri = 2
        ci = 0
        for i in self.days:
            bg = colors["accent"] if i.istoday == True else colors["trans"]
            fg = "#ffffff" if i.isthismonth == True else colors["base"]
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
                        foreground=fg,
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
                        foreground="#ffffff",
                        can_focus=True,
                        mouse_callbacks={
                            "Button1": self.month_back,
                        },
                        )
                    )
        self.controls.append(
                    PopupText(
                        text=self.month_converter(),
                        name = "month",
                        row = 1,
                        col = 3,
                        col_span = 1,
                        h_align="center",
                        highlight=colors["accent"],
                        highlight_method="block",
                        background=colors["trans"],
                        foreground="#ffffff",
                        can_focus=True,
                        mouse_callbacks={
                            "Button1": self.month_back,
                        },
                        )
                    )
        self.controls.append(
                    PopupText(
                        text=">",
                        row = 1,
                        col = 4,
                        col_span = 3,
                        h_align="center",
                        highlight=colors["accent"],
                        highlight_method="block",
                        background=colors["trans"],
                        foreground="#ffffff",
                        can_focus=True,
                        mouse_callbacks={
                            "Button1": self.month_forward,
                        },
                        )
                    )

    def month_back(self):
        if self.month > 1:
            self.month -= 1
            self.reload_calendar()

    def month_forward(self):
        if self.month < 12:
            self.month += 1
            self.reload_calendar()

    def reload_calendar(self):
            self.gen_calendar()
            logger.warning("regenerated calendar")
            for i in self.days:
                if i.name in self.layout._updateable_controls:
                    self.layout._updateable_controls[i.name].text = f"{i.weekday}\n{i.monthday}"
                    self.layout._updateable_controls[i.name].foreground = "#ffffff" if i.isthismonth == True else colors["base"]
                    self.layout._updateable_controls[i.name].background = colors["accent"] if i.istoday == True else colors["trans"]
                else:
                    logger.warning(f"Could not update control {i.name}")

            self.layout._updateable_controls["month"].text = self.month_converter()
            self.layout.draw()
            logger.warning("redrew popup")



    def month_converter(self):
        if self.month == 1:
            return "Jan"
        elif self.month == 2:
            return "Feb"
        elif self.month == 3:
            return "Mar"
        elif self.month == 4:
            return "Apr"
        elif self.month == 5:
            return "May"
        elif self.month == 6:
            return "Jun"
        elif self.month == 7:
            return "Jul"
        elif self.month == 8:
            return "Aug"
        elif self.month == 9:
            return "Sep"
        elif self.month == 10:
            return "Okt"
        elif self.month == 11:
            return "Nov"
        elif self.month == 12:
            return "Dec"


