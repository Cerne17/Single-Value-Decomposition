from part1 import *
from part2 import *

def main(part):
    if part == '1':
        part1()
    else:
        part2()

if __name__ == "__main__":
    part = input("Which Part to Execute? (1 or 2)\n -> ")
    main(part)
