#!/bin/bash
/usr/lib/xfce-polkit/xfce-polkit &
bg.sh &
l.sh &
picom -b &
eww daemon &
dunst &
launch-xob &
networkd-notify &
# kitty --listen-on=unix:@neomutt --class="coms" -e "neomutt" &
# kitty --listen-on=unix:@newsboat --class="coms" -e "newsboat" &
# kitty --listen-on=unix:@ikhal --class="coms" -e "ikhal" &
kitty --listen-on=unix:@btop --class="coms" -e "btop" &
kitty --listen-on=unix:@zabbix --class="mon" -e "zabbixmon" &
kitty --listen-on=unix:@spotify --class="Spotify" -e "spotify_player" &
kitty --listen-on=unix:@neovim --class="neovim" -e "nvim" &
kitty --listen-on=unix:@term --class="term" &
qutebrowser &
