from libqtile.lazy import lazy
from qtile_extras.popup.toolkit import (
    PopupGridLayout,
    PopupImage,
    PopupText
)
from libqtile.resources.utils.settings import colors

def show_power_menu(qtile):

    controls = [
        PopupImage(
            filename="/usr/share/icons/BeautyLine/actions/scalable/lock.svg",
            col=0,
            row=0,
            mouse_callbacks={
                "Button1": lazy.spawn("betterlockscreen -l blur")
            }
        ),
        PopupImage(
            filename="/usr/share/icons/BeautyLine/actions/scalable/system-suspend.svg",
            col=1,
            row=0,
            mouse_callbacks={
                "Button1": lazy.spawn("systemctl suspend")
            }
        ),
        PopupImage(
            filename="/usr/share/icons/BeautyLine/actions/scalable/system-shutdown.svg",
            col=2,
            row=0,
            highlight="A00000",
            mouse_callbacks={
                "Button1": lazy.spawn("systemctl poweroff")
            }
        ),
        PopupImage(
            filename="/usr/share/icons/BeautyLine/actions/scalable/system-reboot.svg",
            col=3,
            row=0,
            highlight="A00000",
            mouse_callbacks={
                "Button1": lazy.spawn("systemctl reboot")
            }
        ),
        PopupImage(
            filename="/usr/share/icons/BeautyLine/actions/scalable/xfsm-logout.svg",
            col=4,
            row=0,
            highlight="A00000",
            mouse_callbacks={
                "Button1": lazy.spawn("loginctl kill-session self")
            }
        ),
        PopupImage(
            filename="/usr/share/icons/BeautyLine/actions/scalable/reload.svg",
            col=5,
            row=0,
            highlight="A00000",
            mouse_callbacks={
                "Button1": lazy.restart()
            }
        ),
        PopupText(
            text="Lock",
            col=0,
            row=1,
            h_align="center"
        ),
        PopupText(
            text="Sleep",
            col=1,
            row=1,
            h_align="center"
        ),
        PopupText(
            text="Shutdown",
            col=2,
            row=1,
            h_align="center"
        ),
        PopupText(
            text="Reboot",
            col=3,
            row=1,
            h_align="center"
        ),
        PopupText(
            text="Leave",
            col=4,
            row=1,
            h_align="center"
        ),
        PopupText(
            text="Reload",
            col=5,
            row=1,
            h_align="center"
        ),
    ]

    layout = PopupGridLayout(
        qtile,
        width=800,
        height=200,
        rows = 2,
        cols = 6,
        controls=controls,
        background=colors["trans"],
        initial_focus=None,
    )

    layout.show(centered=True)
