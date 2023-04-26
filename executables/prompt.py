#!/usr/bin/python
from libqtile.resources.utils.settings import colors
# print(colors)
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
        c_r1,c_g1,c_b1 = self.rgb
        color1 = f"\033[38;2;{c_r1};{c_g1};{c_b1}m"
        c_r2,c_g2,c_b2 = self.rgb2
        color2 = f"\033[38;2;{c_r2};{c_g2};{c_b2}m"
        line = color2 + "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n" if "line" in self.plugins else ""
        spacer = color2 + "┣━━ "
        git = spacer + color1 + "Git Branch: $(git branch 2>/dev/null | grep '^\*' | awk '{print $NF}'  || '') \n" if "git" in self.plugins else ""
        cwd = spacer + color1 + "Current Direcory: \W\n" if "cwd" in self.plugins else ""
        exitcode = spacer + color1 + "Exitcode: $?\n" if "exitcode" in self.plugins else ""
        prompt = color2 + "┗━━━┫ " if "prompt" in self.plugins else ""
        print(f"{line}{cwd}{git}{exitcode}{prompt}{color1}")

#283141
ps1 = Prompt(color=colors["accent"],color2=colors["accent2"],plugins = ["line","prompt","git","cwd","exitcode"])
ps1.construct_prompt()


