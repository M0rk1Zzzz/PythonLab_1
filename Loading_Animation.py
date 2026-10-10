import time

GREEN = '\u001b[42m'
RED = '\u001b[41m'
ERASE = '\x1B[2K'  # cтирает строчку
BEGIN = '\x1B[1G'  #перемещает курсор в начало строки
RESET = '\u001b[0m'

width = 50

def loading():
    for percent in range(0, 110, 10):
        proc = (percent * width) // 100 
        print(f'{ERASE}{BEGIN}Loading ... {GREEN}{" " * proc}{RED}{" " * (width - proc)}{RESET} {percent}%', end='', flush=True)
        time.sleep(0.5)

    print('\nDone!')

loading()