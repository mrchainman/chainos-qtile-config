from libqtile.lazy import lazy
from libqtile.backend.x11.window import Window
from qtile_extras.popup.toolkit import (
    PopupGridLayout,
    PopupText,
    PopupRelativeLayout
)
import calendar
from datetime import date, datetime
from libqtile.resources.utils.settings import colors

cal = calendar.Calendar()
def gen_calendar():
    days = []
    today = date.today()
    i = cal.itermonthdays2(today.year,today.month)
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

def gen_gui(qtile):
    today, days = gen_calendar()
    controls = []
    ri = 0
    ci = 0
    for i,j in days:
        if i == int(today.strftime("%d")):
            bg = colors["accent"]
        else:
            bg = colors["trans"]
        controls.append(
                PopupText(
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


    layout = PopupGridLayout(
        qtile,
        rows=5,
        cols=7,
        width=300,
        height=300,
        controls=controls,
        background=colors["trans"],
        initial_focus=None,
    )

    # layout.show(centered=True)
    layout.show(x=0, y=0, relative_to = 3, relative_to_bar=True)
