WIDTH = 50
RESET = '\033[0m'
GREEN = '\033[42m'   
RED = '\033[41m'  

file = open('sequence.txt', 'r')

main_list = []
list_1 = []
list_2 = []

for number in file:
    main_list.append(number)
    if float(number) != 5 and float(number) > 0:
        list_1.append(number)
    else:
        list_2.append(number)


count_correct = len(list_1) #колво подходящих под условие 
count_incorrect = len(list_2)#колво неподходящих под условие
total = count_correct + count_incorrect

percent_1 = round((count_correct / total) * 100, 1) #процент подходящих под условие
percent_2 = round(100 - percent_1, 1) #процент неподходящих под условие

width_1 = round((percent_1 / 100) * WIDTH)
width_2 = WIDTH - width_1

print('Процентное соотношение')
print(GREEN + ' ' * width_1 + RESET + RED + ' ' * width_2 + RESET)
print(GREEN + ' ' + RESET + f'{percent_1}%')
print(RED + ' ' + RESET + f'{percent_2}%')



