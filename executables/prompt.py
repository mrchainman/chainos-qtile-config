#!/usr/bin/python
from libqtile.resources.utils.settings import colors
import sys
class Prompt():
    def __init__(self,color: str = "#efefef", color2: str = "#bebbeb", prompt_style: str = "default", plugins: list = ["line","prompt"]):
        self.color = color
        self.color2 = color2
        self.prompt_style = prompt_style
        self.plugins = plugins
        self.rgb = self.hex2rgb(color)
        self.rgb2 = self.hex2rgb(color2)

    def hex2rgb(self,col) -> tuple:
        hex = col.lstrip('#')
        return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
        

    def create_colors(self):
        c_r1,c_g1,c_b1 = self.rgb
        self.p_color1 = f"\[\033[38;2;{c_r1};{c_g1};{c_b1}m\["
        c_r2,c_g2,c_b2 = self.rgb2
        self.p_color2 = f"\[\033[38;2;{c_r2};{c_g2};{c_b2}m\["

    def create_utils(self):
        self.line = self.p_color2 + "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n" if "line" in self.plugins else ""
        self.ps1spacerformat = "┣━━ "
        self.ps1spacer = self.p_color2 + self.ps1spacerformat
        self.ps2spacer = ''.join([" " for i in self.ps1spacerformat])

    def construct_prompt(self):
        """
        Unicodes:
━

┏

┃

┓

┗

w

┛

┣

┫

┯

┻



        """
        self.git = self.ps1spacer + self.p_color1 + "Git Branch: $(git branch 2>/dev/null | grep '^\*' | awk '{print $NF}'  || '') \n" if "git" in self.plugins else ""
        self.cwd = self.ps1spacer + self.p_color1 + "Current Direcory: \W\n" if "cwd" in self.plugins else ""
        self.exitcode = self.ps1spacer + self.p_color1 + "Exitcode: $?\n" if "exitcode" in self.plugins else ""
        self.prompt = self.p_color2 + "┗━━━┫ " if "prompt" in self.plugins else ""
        print(f"{self.line}{self.cwd}{self.git}{self.exitcode}{self.prompt}{self.p_color1}")

    def construct_follower(self):
        self.follower = "┗━━━┫ "
        print(f"{self.p_color2}{self.ps2spacer}{self.follower}{self.p_color1}")


#283141
ps1 = Prompt(color=colors["accent"],color2=colors["accent2"],plugins = ["line","prompt","git","cwd","exitcode"])
ps1.create_colors()
ps1.create_utils()
if len(sys.argv) > 1:
    if sys.argv[1] == "ps2":
        ps1.construct_follower()
else:
    ps1.construct_prompt()


