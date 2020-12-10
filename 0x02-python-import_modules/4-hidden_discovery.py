#!/usr/bin/python3
import hidden_4

defined_names = dir(hidden_4)
for name in defined_names:
    if name[:2] != "__":
        print(name)
