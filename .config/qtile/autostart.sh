#!/bin/sh

# systray battery icon
cbatticon -u 5 &

# systray volume
volumeicon &

# Montage de Google-drive
rclone mount --vfs-cache-mode writes drive-general: /home/eddy/Drive/General/ &
rclone mount --vfs-cache-mode writes cnet: /home/eddy/Drive/Cnet/ &
rclone mount --vfs-cache-mode writes eddy-congregacion: /home/eddy/Drive/Eddy-congregacion/ &

# Gestionnaire d' Alimentation
xfce4-power-manager &

# Economiseur d'écran
xfce4-screensaver &

# Theme GTK
#lxappearance &

# Fond d'écran
nitrogen --restore &

# Demande de mot de passe Pamac
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

# Transparence
picom &

# USB - Disques durs externes
udiskie -t &

# Internet
nm-applet &