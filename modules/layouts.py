from libqtile import layout
from libqtile.config import Match

from libqtile.resources.utils.settings import colors

layout_theme = {
    "margin": 20,
    "margin_on_single": True,
    "border_width": 0,
    "border_focus": colors["accent"],
    "border_normal": colors["trans"],
    "border_on_single": True,
    "add_on_top": True,
    "expand": True,
    "master_length": 1,
    "ratio": 0.618,
    "ratio_increment": 0.05,
    "shift_windows": True,
    "font": "Source Code Pro",
    # "font": "JetBrainsMono Nerd Font",
    "grow_amount": 1,
}

layouts = [
    layout.Tile(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.Zoomy(**layout_theme),
    layout.Floating(**layout_theme),
]

floating_layout = layout.Floating(
    **layout_theme,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(wm_class="pinentry-qt"),  # GPG key password entry
        # Match(title="nullplayer"),  # MPV
        # Match(title="Remmina Remote Desktop Client"),
        # Match(wm_class="TeamworkTimer"),  # TW Timer
        # Match(wm_class="Jitsi Meet"),  # Jitsi
        Match(wm_class="iwgtk"),  # Jitsi
        Match(wm_class="proton-bridge"),  # Jitsi
        Match(wm_class="ripdrag"),
        Match(wm_class="net-sourceforge-MSGViewer-ModuleLauncher"),
        Match(wm_class="Display"),
        Match(wm_class="Godot"),
        Match(wm_class="Minetest"),
        Match(wm_class="Steam"),
        # Match(wm_class="Dockx"),
        Match(title="chainos-urlhandler"),  # Custom
        # TODO add matches
    ],
)
