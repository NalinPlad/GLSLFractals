import re

def convert_obsidian_to_md(input_line):
    # Recognize the first pattern and replace it
    r1 = re.compile(r'!\[\[(.*?\.\w+)\|(\d+?)\]\]')
    line = r1.sub(r'<img src="\1" width="\2">', input_line)

    # Recognize the second pattern and replace it
    r2 = re.compile(r'!\[\[(.*?\.\w+)\]\]')
    line = r2.sub(r'<img src="\1">', line)

    return line

with open("jam_obsidian.md", "r") as file:
    lines = file.readlines()
    
conversion = [convert_obsidian_to_md(line) for line in lines]

#bump
with open("jam.md", "w") as output_file:
    output_file.writelines(conversion)
