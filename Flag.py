RED = '\u001b[41m'
WHITE = '\u001b[47m'
BLUE = '\u001b[44m'
RESET = '\u001b[0m'

width = 30
stripes = [(RED, 1), (WHITE, 1), (BLUE, 3), (WHITE, 1), (RED, 1)]

def thai_flag():
    for color, row in stripes:
        line = f'{color}{" " * width}{RESET}\n'
        print(line * row, end='')

thai_flag()