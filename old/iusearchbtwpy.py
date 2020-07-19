#!/usr/bin/python
#
# I Use Arch BTW Interpreter in Python by zamiur
# 
# I use Arch BTW lang specs and original programming lang here
# https://github.com/OverMighty/i-use-arch-btw
#
# Usage: ./i-use-arch-btw-py.py [FILE]

import sys
import getch

def execute(filename):
  f = open(filename, "r")
  evaluate(f.read())
  f.close()


def evaluate(code):
  code     = cleanup(list(code))
  bracemap = buildbracemap(code)

  cells, codeptr, cellptr = [0], 0, 0

  while codeptr < len(code):
    command = code[codeptr]

    if command == "i":
      cellptr += 1
      if cellptr == len(cells): cells.append(0)

    if command == "use":
      cellptr = 0 if cellptr <= 0 else cellptr - 1

    if command == "arch":
      cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < 255 else 0

    if command == "linux":
      cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > 0 else 255

    if command == "by": cells[cellptr] = ord(getch.getch())
    if command == "the" and cells[cellptr] == 0: codeptr = bracemap[codeptr]
    if command == "way" and cells[cellptr] != 0: codeptr = bracemap[codeptr]
    if command == "btw": sys.stdout.write(chr(cells[cellptr]))
    if command == "gentoo": print("I'll add this later")
    
      
    codeptr += 1


def cleanup(code):
  return ''.join(filter(lambda x: x in ['i', 'use', 'arch', 'linux', 'btw', 'by', 'the', 'way'], code))


def buildbracemap(code):
  temp_bracestack, bracemap = [], {}

  for position, command in enumerate(code):
    if command == "the": temp_bracestack.append(position)
    if command == "way":
      start = temp_bracestack.pop()
      bracemap[start] = position
      bracemap[position] = start
  return bracemap


def main():
  if len(sys.argv) == 2: execute(sys.argv[1])
  else: print("Usage:", sys.argv[0], "filename")

if __name__ == "__main__": main()
