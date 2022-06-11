# simple_rsync_backup
Simple rsync backup script

With this script you just provide a source and destination folder. The desination is made to look exactly like the source. This takes the actual command to do tihs and makes it a bit more human-friendly, as well as prevents the potential for mistakes to happen when specifying directoies.

To run this use "python3 backup.py" after opening a terminal in whatever folder you saved it.

Alternativly, you can make a .desktop file in "~/.local/share/applications" and turn it into an application:

~/.local/share/applications/rsync-backup.desktop

[Desktop Entry]<br />
Name=Rsync Backup<br />
Type=Application<br />
Terminal=false<br />
Icon=/path/to/or/name/of/icon/if/you/want/one<br />
Exec=gnome-terminal --title "Backing things up" -- sh -c 'python3 "$HOME/.scripts/backup.py"'<br />

I save my custom scripts in ~/.scripts so that's why the command in Exec= looks the way it does. You can change the directory after "python3" to whereever you store your scripts.
