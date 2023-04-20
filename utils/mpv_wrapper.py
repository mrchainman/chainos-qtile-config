#!/usr/bin/python
from pgrep import pgrep
from os import path
from subprocess import Popen
import socket
from time import sleep

class MpvWrapper():
    def __init__(self, url):
        self.pid = pgrep("mpv")
        self.fifo_file = path.expanduser("~/.config/chainos/mpv/mpv.fifo")
        self.url = url
        self.append_cmd = f'loadfile "{url}" append-play\n'
        self.mpv_cmd = [
                "mpv",
                f"--input-ipc-server={self.fifo_file}",
                "--idle",
                "--title=chainos-video",
                "--ao=pipewire",
                "--framedrop=vo",
                "--video-latency-hacks=yes",
                "--player-operation-mode=pseudo-gui",
                "--geometry=20%x20%+98%+98%",
                "&"
                ]
        print(self.pid)

    def write_to_fifo(self):
        print("Now opening socket")
        with socket.socket(socket.AF_UNIX) as soc:
            soc.connect(self.fifo_file)
            soc.send(str.encode(self.append_cmd))
        # with open(self.fifo_file, 'r', 0) as ff:
        #     ff.write(self.append_cmd)

    def check_mpv(self):
        if len(self.pid) == 0:
            Popen(self.mpv_cmd)
            while True:
                self.pid = pgrep("mpv")
                if len(self.pid) == 1:
                    print(f"Mpv is running with {self.pid}")
                    sleep(1)
                    break

    def append_url(self):
        self.check_mpv()
        self.write_to_fifo()

