#!/usr/bin/python3
import os
import sys

file = os.path.expanduser("~/.config/picom/picom.conf")
# mode = "up"
mode = sys.argv[1]

with open(file, 'r', encoding='utf-8') as f:
    data = f.readlines()
  
for line in data:
    if line.startswith("active-opacity = "):
        activeop,actidx = line, data.index(line)
    elif line.startswith("inactive-opacity = "):
        inactiveop,inactidx = line, data.index(line)


active_current = float(activeop[:-2].split("=")[1])
inactive_current = float(inactiveop[:-2].split("=")[1])

if mode == "up":
    if active_current < 1: 
        active_current += 0.05
        inactive_current += 0.05
    else:
        print("Reached max value")

elif mode == "down":
    if inactive_current > 0: 
        active_current -= 0.05
        inactive_current -= 0.05
    else:
        print("Reached min value")

elif mode == "read":
    pass

data[actidx] = f"active-opacity = {round(active_current,2)} ;\n"
data[inactidx] = f"inactive-opacity = {round(inactive_current,2)} ;\n"


print(f"active current: {round(active_current,2)}")
print(f"inactive current: {round(inactive_current,2)}")


with open(file, 'w', encoding='utf-8') as f:
    f.writelines(data)
