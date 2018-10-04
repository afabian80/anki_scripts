#!/usr/bin/python3

import sys
import os

assert len(sys.argv) == 2

filename = sys.argv[1]
lines = []

with open(filename) as f:
    lines = f.readlines()

for line in lines:
    parts = line.split("\t")
    if(parts == ['\n']):
        continue
    assert len(parts) == 3, line
    hun = parts[1].strip()
    link_orig = parts[2].strip()
    term_and_example = parts[0].split(" ", 1)
    assert len(term_and_example) == 2, line
    eng = term_and_example[0].strip()
    example = term_and_example[1].strip(' ()')
    print("{}\t{}\t{}\t{}".format(eng, example, hun, link_orig))
