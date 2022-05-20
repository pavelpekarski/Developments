#  шаг сдвига в кодировании слова равен длине слова
text = input('Введите текст: ')
s1 = text.split()
s2 = []

u_eng1 = 65                                                                                 #  код из таблицы unicode первого заглвного символа латиницы
u_eng2 = 90                                                                                 #  код из таблицы unicode последнего заглвного символа латиницы
l_eng1 = 97                                                                                 #  код из таблицы unicode первого строчного символа латиницы
l_eng2 = 122                                                                                #  код из таблицы unicode последнего строчного символа латиницы

def cipher(u1, u2, l1, l2):
    for i in range(len(s1)):
        flag = False
        word = s1[i]
        for j in range(len(word)):
            counter = 0
            for x in range(len(word)):
                if word[x] in '.",!#$%&*+-=?@^_0123456789':
                    flag = True
                    counter += 1                                                            #  количество символов, отличных от английских букв
            ordinata = ord(word[j])
            
            if word[j] in  ' .",!#$%&*+-=?@^_0123456789':
                s2.append(chr(ordinata))
                continue
            if flag == True:
                if word[j] == word[j].upper():                                              #  условия символов для верхнего регистра
                    if ord(word[j]) + len(word) - counter <= u2:                            #  проверка не выхода символа из диапазона кодов верхнего регистра после сдвига
                        s2.append(chr(ordinata + len(word) - counter))
                    else:
                        s2.append(chr((ordinata + len(word) - counter) % u2 + (u1 - 1)))    #  в случае выхода из диапазона кодов верхнего регистра после добавления сдвига, продолжаем счет с первого
                if word[j] == word[j].lower():                                              #  условия символов для нижнего регистра
                    if ord(word[j]) + len(word) - counter <= l2:                            #  проверка не выхода символа из диапазона кодов нижнего регистра после сдвига
                        s2.append(chr(ordinata + len(word) - counter))
                    else:
                        s2.append(chr((ordinata + len(word) - counter) % l2 + (l1 - 1)))    #  в случае выхода из диапазона кодов нижнего регистра после добавления сдвига, продолжаем счет с первого
            elif flag == False:
                if word[j] == word[j].upper():                                              #  условия символов для верхнего регистра
                    if ord(word[j]) + len(word) <= u2:                                      #  проверка не выхода символа из диапазона кодов верхнего регистра после сдвига
                        s2.append(chr(ordinata + len(word)))
                    else:
                        s2.append(chr((ordinata + len(word)) % u2 + (u1 - 1)))              #  в случае выхода из диапазона кодов верхнего регистра после добавления сдвига, продолжаем счет с первого
                if word[j] == word[j].lower():                                              #  условия символов для нижнего регистра
                    if ord(word[j]) + len(word) <= l2:                                      #  проверка не выхода символа из диапазона кодов нижнего регистра после сдвига
                        s2.append(chr(ordinata + len(word)))
                    else:
                        s2.append(chr((ordinata + len(word)) % l2 + (l1 - 1)))              #  в случае выхода из диапазона кодов нижнего регистра после добавления сдвига, продолжаем счет с первого
        s2.append(' ')
    return s2[:-1]

print(*cipher(u_eng1, u_eng2, l_eng1, l_eng2), sep='')