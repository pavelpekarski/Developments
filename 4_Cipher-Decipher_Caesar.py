s = []
u_rus1 = 1040                                                                   #  код из таблицы unicode первого заглвного символа кириллицы
u_rus2 = 1071                                                                   #  код из таблицы unicode последнего заглвного символа кириллицы
l_rus1 = 1072                                                                   #  код из таблицы unicode первого строчного символа кириллицы
l_rus2 = 1103                                                                   #  код из таблицы unicode последнего строчного символа кириллицы
u_eng1 = 65                                                                     #  код из таблицы unicode первого заглвного символа латиницы
u_eng2 = 90                                                                     #  код из таблицы unicode последнего заглвного символа латиницы
l_eng1 = 97                                                                     #  код из таблицы unicode первого строчного символа латиницы
l_eng2 = 122                                                                    #  код из таблицы unicode последнего строчного символа латиницы

def is_valid(num):
    while not num.isdigit() or num not in '1' and num not in '2':
        num = input('Некорректное значение. Необходимо ввести 1 или 2: ')
    num = int(num)
    return num

def is_valid_step(num):
    while not num.isdigit():
        num = input('Некорректное значение. Необходимо ввести число: ')
    num = int(num)
    return num

def cipher(u1, u2, l1, l2):
    for i in range(len(s3)):
        ordinata = ord(s3[i])
        if s3[i] in ' .",!#$%&*+-=?@^_0123456789':
            s.append(chr(ordinata))
        elif s3[i] == s3[i].upper():                                            #  условия символов для верхнего регистра
            if ord(s3[i]) + k <= u2:                                            #  проверка не выхода символа из диапазона кодов верхнего регистра после сдвига
                s.append(chr(ordinata + k))
            else:
                s.append(chr((ordinata + k) % u2 + (u1 - 1)))                   #  в случае выхода из диапазона кодов верхнего регистра после добавления сдвига, продолжаем счет с первого
        elif s3[i] == s3[i].lower():                                            #  условия символов для нижнего регистра
            if ord(s3[i]) + k <= l2:                                            #  проверка не выхода символа из диапазона кодов нижнего регистра после сдвига
                s.append(chr(ordinata + k))
            else:
                s.append(chr((ordinata + k) % l2 + (l1 - 1)))                   #  в случае выхода из диапазона кодов нижнего регистра после добавления сдвига, продолжаем счет с первого
    return s

def decipher(u1, u2, l1, l2):                                                   #  функция дешифрования
    for i in range(len(s3)):
        ordinata = ord(s3[i])
        if s3[i] in ' .",!#$%&*+-=?@^_0123456789':
            s.append(chr(ordinata))
        elif s3[i] == s3[i].upper():                                            #  условия символов для верхнего регистра
            if ord(s3[i]) - k >= u1:                                            #  проверка не выхода символа из диапазона кодов верхнего регистра после сдвига
                s.append(chr(ordinata - k))
            else:
                s.append(chr((ordinata - k) + (u2 - u1 + 1)))                   #  в случае выхода из диапазона кодов верхнего регистра после добавления сдвига, добавляем мощность алфавита
        elif s3[i] == s3[i].lower():                                            #  условия символов для нижнего регистра
            if ord(s3[i]) - k >= l1:                                            #  проверка не выхода символа из диапазона кодов нижнего регистра после сдвига
                s.append(chr(ordinata - k))
            else:
                s.append(chr((ordinata - k) + (l2 - l1 + 1)))                   #  в случае выхода из диапазона кодов нижнего регистра после добавления сдвига, добавляем мощность алфавита
    return s

n1 = input('Введите направление (шифрование - 1 \ дешифрование - 2): ')
s1 = is_valid(n1)

n2 = input('Введите язык алфавита (rus - 1 \ eng - 2): ')
s2 = is_valid(n2)

n3 = input('Введите шаг сдвига: ')
k = is_valid_step(n3)

s3 = input('Введите текст: ')

if s1 == 1:
    if s2 == 1:
        print(*cipher(u_rus1, u_rus2, l_rus1, l_rus2), sep='')
    elif s2 == 2:
        print(*cipher(u_eng1, u_eng2, l_eng1, l_eng2), sep='')
elif s1 == 2:
    if s2 == 1:
        print(*decipher(u_rus1, u_rus2, l_rus1, l_rus2), sep='')
    elif s2 == 2:
        print(*decipher(u_eng1, u_eng2, l_eng1, l_eng2), sep='')