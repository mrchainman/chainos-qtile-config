from libqtile.lazy import lazy
from libqtile.backend.x11.window import Window
from qtile_extras.popup.toolkit import (
    PopupText,
    PopupWidget,
    PopupGridLayout,
)
from libqtile import widget
import time
from libqtile.resources.utils.settings import colors

from libqtile.log_utils import logger
import calendar




import sys
import datetime
import time
import os
sys.path.append(os.path.expanduser("~/.data/Development/ChainOS/chainos-packages/python-libs/chainos_python_libs/work/"))
import office365


class Events():
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
            self.account = office365.OfficeAccount()
            self.gen_all()
            self.gen_layout(qtile)
            self.show_layout()

    def gen_all(self):
            self.controls = []
            self.events = []
            self.get_events()
            self.gen_events_gui()

    def get_events(self):
        for i in self.account.cal_get_all():
            if i.start.timestamp() > datetime.datetime.now().timestamp():
                # print(f"{i.start}: {i.subject} {i.online_meeting_url if i.is_online_meeting else i.location['displayName']}")
                self.events.append(i)


    def show_layout(self):
        self.layout.show(x=0, y=0, relative_to = 3, relative_to_bar=True)

    def gen_layout(self,qtile):
        self.layout = PopupGridLayout(
                            qtile,
                            rows=7,
                            cols=3,
                            width=400,
                            height=300,
                            controls=self.controls,
                            background=colors["trans"],
                            initial_focus=None,
                            close_on_click=False,
                            )

    def gen_events_gui(self):
        ri = 0
        self.sorted_events = sorted(self.events, key= lambda x: x.start)
        for i in self.sorted_events:
            # bg = colors["accent"] if i.istoday == True else colors["trans"]
            # fg = "#ffffff" if i.isthismonth == True else colors["base"]
            bg = colors["trans"]
            fg = colors["accent"]
            self.controls.append(
                    PopupText(
                        name= str(i.ical_uid).join("_date"),
                        text=f"{i.start.strftime('%H:%M')}",
                        row = ri,
                        col = 0,
                        width=0.5,
                        height=0.1,
                        h_align="center",
                        highlight=colors["accent"],
                        highlight_method="block",
                        foreground=fg,
                        background=bg,
                        can_focus=False,
                        mouse_callbacks={
                            # "Button1": qtile.cmd_spawn(f"kitty khal at {i}/{today.month}/{today.year}"),
                        },
                        )
                    )
            self.controls.append(
                    PopupText(
                        name= str(i.ical_uid).join("_subj"),
                        text=f"{i.subject}",
                        row = ri,
                        col = 1,
                        width=0.8,
                        height=0.1,
                        h_align="center",
                        highlight=colors["accent"],
                        highlight_method="block",
                        foreground=fg,
                        background=bg,
                        can_focus=False,
                        mouse_callbacks={
                            # "Button1": qtile.cmd_spawn(f"kitty khal at {i}/{today.month}/{today.year}"),
                        },
                        )
                    )
            self.controls.append(
                    PopupText(
                        name= str(i.ical_uid).join("_location"),
                        text=f"{i.online_meeting_url if i.is_online_meeting else i.location['displayName']}",
                        row = ri,
                        col = 2,
                        width=0.8,
                        height=0.1,
                        h_align="center",
                        highlight=colors["accent"],
                        highlight_method="block",
                        foreground=fg,
                        background=bg,
                        can_focus=True,
                        mouse_callbacks={
                            "Button1": lazy.spawn(f"/opt/appimages/teams-for-linux.AppImage {i.online_meeting_url}"),
                        },
                        )
                    )
            ri += 1
