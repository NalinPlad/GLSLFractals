import re

def convert_obsidian_to_md(input_line):
    # Recognize the first pattern and replace it
    r1 = re.compile(r'!\[\[(.*?\.\w+)\|(\d+?)\]\]')
    line = r1.sub(r'![\1](\1){:width="\2px"}', input_line)

    # Recognize the second pattern and replace it
    r2 = re.compile(r'!\[\[(.*?\.\w+)\]\]')
    line = r2.sub(r'![\1](\1)', line)

    return line

with open("Jam.md", "r") as file:
    lines = file.readlines()
    
conversion = [convert_obsidian_to_md(line) for line in lines]

with open("Jam_md.md", "w") as output_file:
    output_file.writelines(conversion)

