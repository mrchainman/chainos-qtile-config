# Testing:
Xephyr -br -ac -noreset -screen 1280x720 :1
DISPLAY=:1 qtile start




# TODOS:
- [ ] Update image widget dinamycally
- [ ] Bluetooth widget
- [ ] Wifi widget
- [ ] Battery Widget
- [ ] Keyboard Widget
- [ ] Audio Widget


# Updating images:

Get a list of statusbar widgets with list_widgets()
Update the coresponding widget with
qtile cmd-obj -o widget '<image>' -f update -a <path/to/image>
