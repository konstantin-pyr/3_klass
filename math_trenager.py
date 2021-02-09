import random
from tkinter import Tk,simpledialog,messagebox

def examle_create():
    '''Функция задает случайные числа и ставит большее первым. 
    Для сложения x1 и x2, для умножения y1 и y2.'''
    x1 = random.randint(0,100)
    x2 = random.randint(0,100)
    y1 =  random.randint(0,10)
    y2 =  random.randint(0,10)
    if x1 < x2:
        x1,x2 = x2,x1
    return x1, x2, y1, y2


def proveryalka(x1, x2, answer, operator):
    '''Проверяет правильность ответа пользователя и выводит результаты проверки.'''
    if (operator == '-') & ((x1-x2) == answer):
        messagebox.showinfo('Итог', 'Правильно!')
    elif (operator == '+') & ((x1+x2) == answer):
        messagebox.showinfo('Итог', 'Правильно!')
    elif (operator == '*') & ((x1*x2)==answer):
         messagebox.showinfo('Итог', 'Правильно!')
    else: 
        messagebox.showinfo('Итог', 'Неправильно')
 
root = Tk() # Создает пустое окно Tkinter
root.withdraw() # Прячет окно Tkinter

# Запускаем бесконечный цикл для тренировки устного счета
while True:
    x1, x2, y1, y2 = examle_create()
    operator = random.choice(['-','+','*'])
    if operator in ['-','+']:
        example = str(x1) + (operator) + str(x2)
    elif operator in ['*']:
        example = str(y1) + (operator) + str(y2)

    answer = simpledialog.askstring('Запишите ответ', example) # Выводим окно с примером
    answer = int(answer) # Переводим ответ в целое число
    
    # Проверяем правильность решения
    if operator in ['-','+']:
        proveryalka(x1, x2, answer, operator)
    elif operator in ['*']:
        proveryalka(y1, y2, answer, operator)
