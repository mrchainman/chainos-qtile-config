#!/usr/bin/python
from libqtile.resources.utils.settings import colors
import sys
class Prompt():
    """
    Defines the full Bashprompt
    """
    def __init__(self,color: str = "#efefef", color2: str = "#bebbeb", prompt_style: str = "default", plugins: list = [[]], show_line: bool = False, show_line_head: bool = False, show_prompt: bool = True ):
        self.color = color
        self.color2 = color2
        self.prompt_style = prompt_style
        self.plugins = plugins
        self.show_line = show_line
        self.show_line_head = show_line_head
        self.show_prompt = show_prompt
        self.rgb = self.hex2rgb(color)
        self.rgb2 = self.hex2rgb(color2)

    def hex2rgb(self, col: str) -> tuple:
        """
        Convert a hexcolorstring to rbg.
        """
        hex = col.lstrip('#')
        rgbs = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
        return rgbs
        

    def construct_prompt(self):
        """
        Construct all the parts used in the prompt. 
        """
        c_r1,c_g1,c_b1 = self.rgb
        self.p_color1 = f"\[\033[38;2;{c_r1};{c_g1};{c_b1}m\["
        c_r2,c_g2,c_b2 = self.rgb2
        self.p_color2 = f"\[\033[38;2;{c_r2};{c_g2};{c_b2}m\["

        #< ~/test | sed 's/0/━/g')
        self.char_creator = "$(for i in $(seq $(expr $COLUMNS - 2)); do echo -n '━' ; done)"
        self.line_head = self.p_color2 + "┏" + self.char_creator + "┓\n"
        self.line = self.p_color2 + "┣" + self.char_creator + "┫\n"
        self.spacerbeginning = "┣━┫ "
        self.spacerend = " ┣━┫"
        self.spacermiddle = " ┣━┫ "
        self.spacerblank = ''.join([" " for i in self.spacermiddle])
        self.newline = "\n"

        self.prompt = self.p_color2 + "┗━━━┫ "
        self.follower = self.p_color2 + self.spacerblank + "┗━━━┫ "

        self.git = "Git Branch: $(git branch 2>/dev/null | grep '^\*' | awk '{print $NF}') Modified Files: $(git status --short 2>/dev/null | wc -l) Last Commit: $(git show --oneline 2>/dev/null | head -n 1)"
        self.cwd = "Current Direcory: \W"
        self.exitcode = "Exitcode: $?"
        self.packages = "Packages: $(pacman -Q | wc -l)"
        self.amiroot = "User: $(whoami)"
        self.updates = "Updates: $(checkupdates | wc -l)"



    def generate_complete_prompt(self) -> list:
        """
        Generates a list containing all the parts used in the prompt.
        """
        self.construct_prompt()
        self.full_prompt = []
        for lst in self.plugins:
            for i in lst:
                self.full_prompt.append(self.p_color2)
                if lst.index(i) == 0:
                    self.full_prompt.append(self.spacerbeginning)
                else:
                    self.full_prompt.append(self.spacermiddle)
                self.full_prompt.append(self.p_color1)
                self.full_prompt.append(getattr(self,i))
            # self.full_prompt.append(self.spacerend)
            self.full_prompt.append(self.p_color2)
            self.full_prompt.append(self.newline)
            if self.show_line:
                self.full_prompt.append(self.line)

        if self.show_line_head:
            self.full_prompt.insert(0, self.line_head)
        if self.show_prompt:
            self.full_prompt.append(self.prompt)
            self.full_prompt.append(self.p_color1)
        return self.full_prompt


    def show_ps1(self) -> str:
        """
        Converts the list of prompts to one single string for PS1
        """
        self.generate_complete_prompt()
        string = ''.join(self.full_prompt)
        return string

    def show_follower(self) -> str:
        """
        Converts the list of prompts to one single string for PS2
        """
        self.generate_complete_prompt()
        string = self.follower
        return string


ps1 = Prompt(
        color=colors["accent"],
        color2=colors["accent2"],
        plugins = [
            ["cwd", "git"],
            ["amiroot", "exitcode","packages",],
            ],
        show_line = True,
        show_line_head = True,
        show_prompt = True,
        )

if len(sys.argv) > 1:
    if sys.argv[1] == "ps2":
        print(ps1.show_follower())
else:
    print(ps1.show_ps1())


