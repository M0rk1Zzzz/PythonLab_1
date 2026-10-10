WHITE = '\u001b[47m'
BLACK = '\u001b[40m'
RESET = '\u001b[0m'

width = 55           
half = 2             
center = width // 2
offsets = [0, 1, 2, 4, 6, 9, 13, 18, 23] #расстояние смещения от центра

def shape(offset):
    line = ''
    for x in range(width):
        distance = abs(x - center) #модуль для симметричности
        if abs(distance - offset) <= half:
            line += f'{WHITE} '
        else:
            line += f'{BLACK} '
    return line + RESET

for offset in offsets:
    print(shape(offset))