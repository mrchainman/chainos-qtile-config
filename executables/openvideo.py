#!/usr/bin/python
from libqtile.resources.utils.mpv_wrapper import MpvWrapper

def mpv_run(url = ""):
    mpvinstance = MpvWrapper(url)
    mpvinstance.append_url()

if __name__ == "__main__":
    import sys
    mpv_run(url = sys.argv[1])



