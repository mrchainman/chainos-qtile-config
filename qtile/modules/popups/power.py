from libqtile.lazy import lazy
from qtile_extras.popup.toolkit import (
    PopupRelativeLayout,
    PopupImage,
    PopupText
)
from utils.settings import colors

def show_power_menu(qtile):

    controls = [
        PopupImage(
            filename="/etc/chainos/qtile/icons/lock.svg",
            pos_x=0.05,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            mouse_callbacks={
                "Button1": lazy.spawn("betterlockscreen -l blur")
            }
        ),
        PopupImage(
            filename="/etc/chainos/qtile/icons/sleep.svg",
            pos_x=0.25,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            mouse_callbacks={
                "Button1": lazy.spawn("systemctl suspend")
            }
        ),
        PopupImage(
            filename="/etc/chainos/qtile/icons/shutdown.svg",
            pos_x=0.45,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            highlight="A00000",
            mouse_callbacks={
                "Button1": lazy.shutdown()
            }
        ),
        PopupImage(
            filename="/etc/chainos/qtile/icons/reboot.svg",
            pos_x=0.65,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            highlight="A00000",
            mouse_callbacks={
                "Button1": lazy.spawn("systemctl reboot")
            }
        ),
        PopupImage(
            filename="/etc/chainos/qtile/icons/leave.svg",
            pos_x=0.85,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            highlight="A00000",
            mouse_callbacks={
                "Button1": lazy.spawn("loginctl kill-session self")
            }
        ),
        PopupText(
            text="Lock",
            pos_x=0.05,
            pos_y=0.7,
            width=0.1,
            height=0.2,
            h_align="center"
        ),
        PopupText(
            text="Sleep",
            pos_x=0.25,
            pos_y=0.7,
            width=0.1,
            height=0.2,
            h_align="center"
        ),
        PopupText(
            text="Shutdown",
            pos_x=0.45,
            pos_y=0.7,
            width=0.1,
            height=0.2,
            h_align="center"
        ),
        PopupText(
            text="Reboot",
            pos_x=0.65,
            pos_y=0.7,
            width=0.1,
            height=0.2,
            h_align="center"
        ),
        PopupText(
            text="Leave",
            pos_x=0.85,
            pos_y=0.7,
            width=0.1,
            height=0.2,
            h_align="center"
        ),
    ]

    layout = PopupRelativeLayout(
        qtile,
        width=800,
        height=200,
        controls=controls,
        background=colors["trans"],
        initial_focus=None,
    )

    layout.show(centered=True)
