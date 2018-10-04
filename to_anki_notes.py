#!/usr/bin/python3

import sys
import os

assert len(sys.argv) == 3

filename = sys.argv[1]
tag = sys.argv[2]
lines = []
commands = []
download_file = "download_media_{}.sh".format(tag)

with open(filename) as f:
    lines = f.readlines()

print("tags:{}".format(tag))

for line in lines:
    parts = line.split("\t")
    if(parts == ['\n']):
        continue
    assert len(parts) == 5, line
    eng = parts[0].strip()
    ipa = parts[1].strip()
    example = parts[2].strip()
    hun = parts[3].strip()
    link_orig = parts[4].strip()
    ext = link_orig.split(".")[-1]
    link_anki="<img src=\"{}.{}\">".format(eng, ext)
    print("{}\t{}\t{}\t{}\t{}".format(eng, ipa, example, hun, link_anki))
    cmd = "wget -q -O media/{}.{} {}".format(eng, ext, link_orig)
    commands.append(cmd)

with open(download_file, 'w') as f:
    f.write("#!/bin/bash -eux\n")
    for command in commands:
        f.write(command)
        f.write("\n")

os.chmod(download_file, 0o755)