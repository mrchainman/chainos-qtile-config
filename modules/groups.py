from libqtile.config import Group, Key, Match, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.resources.utils.settings import workspace_names
from libqtile.resources.utils.presets import chinese, numbers, smileys
from libqtile.resources.modules.keys import keys, mod, shift, alt
# from libqtile.backend.base import Window, Internal
# from libqtile import hook

# @hook.subscribe.setgroup
# def mpv_follow():
#     for w in qtile.windows_map.values():
#         if not isinstance(w, Internal):
#             if w.get_wm_class() == "mpv":
#                 w.togroup()

workspaces = [
    {
        "name": workspace_names[0],
        "key": "1",
        "lay": "bsp",
        "matches":[
            Match(wm_class="qutebrowser"),
            ],
    },
    {
        "name": workspace_names[1],
        "key": "2",
        "lay": "bsp",
        "matches":[
            Match(wm_class="Microsoft Teams - Preview"),
            ],
    },
    {
        "name": workspace_names[2],
        "key": "3",
        "lay": "bsp",
        "matches":[
            Match(wm_class="TeamworkTimer")
            ]
    },
    {
        "name": workspace_names[3],
        "key": "4",
        "lay": "matrix",
        "matches":[
            Match(wm_class="coms"),
            ],
    },
    {
        "name": workspace_names[4],
        "key": "5",
        "lay": "bsp",
    },
    {
        "name": workspace_names[5],
        "key": "6",
        "lay": "bsp",
    },
    {
        "name": workspace_names[6],
        "key": "7",
        "lay": "bsp",
    },
    {
        "name": workspace_names[7],
        "key": "8",
        "lay": "bsp",
    },
    {
        "name": workspace_names[8],
        "key": "9",
        "lay": "bsp",
        "matches": [
            Match(wm_class="Spotify"),
            Match(wm_class="Nchat"),
            Match(wm_class="Igdm"),
            ],
    },
    {
        "name": workspace_names[9],
        "key": "0",
        "lay": "floating",
    },
]

for i in chinese:
    lazy.delgroup(i)
for i in numbers:
    lazy.delgroup(i)
for i in smileys:
    lazy.delgroup(i)

groups = [Group(i) for i in workspace_names]

for workspace in workspaces:
    matches = workspace["matches"] if "matches" in workspace else None
    lay = workspace["lay"] if "lay" in workspace else "bsp"
    keep = workspace["keep"] if "keep" in workspace else True
    start = workspace["start"] if "start" in workspace else True
    groups.append(Group(workspace["name"], matches=matches, layout=lay, persist=keep, init=False))
    keys.append(
        Key(
            [mod],
            workspace["key"],
            lazy.group[workspace["name"]].toscreen(toggle=True),
            desc="Focus this desktop",
        )
    )
    keys.append(
        Key(
            [mod, shift],
            workspace["key"],
            *(
                lazy.window.togroup(workspace["name"]),
                lazy.group[workspace["name"]].toscreen(toggle=True),
            ),
            desc="Move focused window to another group",
        )
    )

groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown(
                "term",
                "kitty --listen-on=unix:@scratch",
                opacity=0.5,
                x=0.1,
                y=0.15,
                width=0.8,
                height=0.7,
                on_focus_lost_hide=False,
            ),
            DropDown(
                "mpv",
                "mpv  --input-ipc-server='/home/davidc/.config/chainos/mpv/mpv.fifo' --idle --ao=pulse --framedrop=vo --video-latency-hacks=yes --player-operation-mode=pseudo-gui",
                x=0.62,
                y=0.60,
                width=0.35,
                height=0.35,
                on_focus_lost_hide=False,
            ),
        ],
)
)
