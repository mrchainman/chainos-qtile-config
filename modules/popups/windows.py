from libqtile.lazy import lazy
from libqtile.backend.x11.window import Window
from qtile_extras.popup.toolkit import (
    PopupGridLayout,
    PopupText,
    PopupImage,
)
import os
from libqtile.resources.utils.settings import colors, stickys, app_img_maps
from libqtile.log_utils import logger


def wrapperstuff(win):
    group = win.group
    name = win.name
    group.toscreen()
    group.focus_by_name(name)

def get_image(cls):
    path = "/usr/share/icons/BeautyLine/apps/scalable"
    fallback = f"{path}/python.svg"
    image = ""
    for name in cls:
        try_image = f"{path}/{str(name).lower()}.svg"
        if os.path.isfile(try_image):
             image = try_image
             break
        else:
            continue
    if image == "":
        for name in cls:
            if name in app_img_maps.keys():
                image = f"{path}/{app_img_maps[name]}.svg"
                break
            else:
                logger.warning(f"could not find image for any of {cls}, using fallback ({fallback})")
                image = fallback
    return image


def show_windows_menu(qtile):
    controls = []
    ri = 0
    ci = 0
    for i in qtile.windows_map.values():
        if isinstance(i, Window):
            # logger.warning(type(i.group.name))
            if i.group.name == "scratchpad":
                continue

            elif i.name in stickys:
                continue
            elif not set(i._wm_class).isdisjoint(stickys):
                continue
            else:
                controls.append(
                        PopupImage(
                            filename = get_image(i._wm_class),
                            row = ri,
                            col = ci,
                            background=colors["trans"],
                            ),
                        )
                ri += 1
                controls.append(
                        PopupText(
                            text= f"  {str(i.name)[:15]}  ",
                            row = ri,
                            col = ci,
                            width=0.1,
                            height=1,
                            h_align="center",
                            highlight=colors["accent"],
                            highlight_method="block",
                            background=colors["trans"],
                            can_focus=True,
                            mouse_callbacks={
                                "Button1": lambda value=i: wrapperstuff(value),
                            },
                            )
                        )
                ri -= 1
                if ci < 4:
                    ci += 1
                else:
                    ri += 2
                    ci = 0

    layout = PopupGridLayout(
        qtile,
        rows=10,
        cols=5,
        width=1000,
        height=500,
        controls=controls,
        background=colors["trans"],
        initial_focus=None,
    )

    layout.show(centered=True)
