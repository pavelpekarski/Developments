import random
print('Добро пожаловать в цифровую угодайку')
x = input('Введите правую границу диапазона случайного выбора числа: ')
while not x.isdigit():
    x = input('Введите число: ')
x = int(x)
n = random.randint(1, x)
print('Случайное число:', n)

def is_valid(num):
    while not num.isdigit() or int(num) not in range(1, x + 1):
        print('А может быть все-таки введем целое число от 1 до', x, '?')
        num = input()
    num = int(num)
    if 1 <= num <= x:
        return True, num
    else:
        return False

counter = 0
while True:
    print('Введите число в диапазоне от 1 до', x)
    num = input()
    counter += 1
    flag, num_valid = is_valid(num)
    if flag == True:
        num_valid = int(num_valid)
        if num_valid < n:
            print()
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif num_valid > n:
            print()
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print()
            print('Вы угадали, поздравляем!')
            print('Количество попыток:', counter)
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            print()
            s = input('Сыграем еще раз? (y - да / n - нет) ')
            if s == 'y':
                x = input('Введите правую границу диапазона случайного выбора числа: ')
                while not x.isdigit():
                    x = input('Введите число: ')
                x = int(x)
                n = random.randint(1, x)
                print('Случайное число:', n)
                continue
            elif s == 'n':
                print('До новых встреч!')
                break