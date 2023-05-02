from libqtile.config import Group, Key, Match, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.resources.utils.settings import workspace_names
from libqtile.resources.utils.presets import chinese, numbers, smileys
from libqtile.resources.modules.keys import keys, mod, shift, alt


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
            Match(wm_class="ferdium"),
            ],
    },
    {
        "name": workspace_names[2],
        "key": "3",
        "lay": "bsp",
        "matches":[
            Match(wm_class="firefox-esr"),
            ]
    },
    {
        "name": workspace_names[3],
        "key": "4",
        "lay": "bsp",
        "matches":[
            Match(wm_class="coms"),
            ],
    },
    {
        "name": workspace_names[4],
        "key": "5",
        "lay": "bsp",
        "matches":[
            Match(wm_class="ipy"),
            ],
    },
    {
        "name": workspace_names[5],
        "key": "6",
        "lay": "bsp",
        "matches":[
            Match(wm_class="vifm"),
            ],
    },
    {
        "name": workspace_names[6],
        "key": "7",
        "lay": "bsp",
        "matches":[
            Match(wm_class="Zathura"),
            ],
    },
    {
        "name": workspace_names[7],
        "key": "8",
        "lay": "bsp",
        # "matches":[
        #     ],
    },
    {
        "name": workspace_names[8],
        "key": "9",
        "lay": "bsp",
        "matches":[
            Match(wm_class="Steam"),
            ],
    },
    {
        "name": workspace_names[9],
        "key": "0",
        "lay": "zoomy",
        "matches": [
            Match(wm_class="qpwgraph"),
            Match(wm_class="jamesdsp"),
            Match(wm_class="easyeffects"),
            Match(wm_class="NoiseTorch"),
            ],
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
    lay = workspace["lay"]
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
                "alacritty",
                opacity=0.5,
                x=0.05,
                y=0.05,
                width=0.4,
                height=0.4,
                on_focus_lost_hide=False,
            ),
            DropDown(
                "ipy",
                "alacritty -e ipython",
                opacity=0.5,
                x=0.05,
                y=0.55,
                width=0.4,
                height=0.4,
                on_focus_lost_hide=False,
            ),
            DropDown(
                "nvim",
                "alacritty -e nvim ~/.data/editornotes",
                opacity=0.5,
                x=0.5,
                y=0.05,
                width=0.42,
                height=0.6,
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
            DropDown(
                "twtimer",
                "teamworktimer",
                x=0.5,
                y=0.3,
                width=0.4,
                height=0.3,
                on_focus_lost_hide=False,
            ),
            DropDown(
                "keepass",
                "keepassxc",
                x=0.5,
                y=0.47,
                width=0.4,
                height=0.3,
                on_focus_lost_hide=False,
            ),
            DropDown(
                "qtpass",
                "qtpass",
                x=0.5,
                y=0.47,
                width=0.4,
                height=0.3,
                on_focus_lost_hide=False,
            ),
            DropDown(
                "joplin",
                "joplin-desktop",
                opacity=0.5,
                x=0.5,
                y=0.05,
                width=0.42,
                height=0.6,
                on_focus_lost_hide=False,
            ),
            DropDown(
                "pcmanfm",
                "pcmanfm",
                x=0.55,
                y=0.50,
                width=0.4,
                height=0.4,
                on_focus_lost_hide=False,
            ),
            DropDown(
                "ferdium",
                "ferdium",
                opacity=0.5,
                x=0.05,
                y=0.05,
                width=0.6,
                height=0.6,
                on_focus_lost_hide=False,
            ),
            DropDown(
                "myxer",
                "myxer",
                x=0.55,
                y=0.50,
                width=0.4,
                height=0.4,
                on_focus_lost_hide=False,
            ),
            DropDown(
                "bluetooth",
                "blueman-manager",
                opacity=0.5,
                x=0.69,
                y=0.01,
                width=0.30,
                height=0.6,
                on_focus_lost_hide=False,
            ),

            DropDown(
                "wifi",
                "iwgtk",
                opacity=0.5,
                x=0.69,
                y=0.01,
                width=0.30,
                height=0.6,
                on_focus_lost_hide=False,
            ),

            DropDown(
                "arandr",
                "arandr",
                opacity=0.5,
                x=0.69,
                y=0.01,
                width=0.30,
                height=0.6,
                on_focus_lost_hide=False,
            )

        ],
)
)
