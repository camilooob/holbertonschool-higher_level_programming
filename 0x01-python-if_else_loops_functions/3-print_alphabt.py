#!/usr/bin/python3
for i in range(ord('a'), ord('{')):
    if i == 113 or i == 101:
        continue
    print("{0:s}".format(chr(i)), end='')
