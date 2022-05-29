import random
word_list = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги', 'земля', 'машина', 'вода', 'отец', 'проблема', 'вариант', 'министр', 'граница', 'дух', 'модель', 'операция', 'пара', 'сон', 'название', 'ум', 'повод', 'старик', 'миллион', 'успех', 'счастье', 'ребята', 'кабинет', 'магазин', 'пространство', 'выход', 'удар', 'база', 'знание', 'текст', 'защита', 'руководство', 'площадь', 'сознание', 'возраст', 'участник', 'участок','пункт', 'линия', 'желание', 'папа', 'доктор', 'губа', 'дочь', 'среда', 'председатель', 'представление', 'солдат', 'художник', 'волос', 'оружие', 'соответствие', 'ветер', 'парень', 'зрение', 'генерал', 'огонь', 'понятие', 'строительство', 'ухо', 'грудь', 'нос', 'страх', 'услуга', 'содержание', 'радость', 'велосипед', 'петрушка']

def get_word():
    return random.choice(word_list).upper()

def display_hangman(tries):
    stages = [
    # (0) голова, туловище, обе руки, обе ноги
    ''' 
    ------------
    |          |
    |          O
    |         \\|/
    |          |
    |         / \\
    - 
    ''',
    # (1) голова, туловище, обе руки, одна нога]
    '''
    ------------
    |          |
    |          O
    |         \\|/
    |          |
    |         /
    - 
    ''',
    # (2) голова, туловище, обе руки, без ног]
    ''' 
    ------------
    |          |
    |          O
    |         \\|/
    |          |
    |
    - 
    ''',
    # (3) голова, туловище, одна рука, без ног]
    ''' 
    ------------
    |          |
    |          O
    |         \\|
    |          |
    |
    - 
    ''',
    # (4) голова, туловище, без рук, без ног]
    ''' 
    ------------
    |          |
    |          O
    |          |
    |          |
    |
    - 
    ''',
    # (5) голова, без туловища, без рук, без ног]
    '''
    ------------
    |          |
    |          O
    |
    |
    |
    - 
    ''',
    # (6) без головы, без туловища, без рук, без ног]
    ''' 
    ------------
    |          |
    |
    |
    |
    |
    - 
    '''
    ]
    return stages[tries]

def yes_or_no():
    answer = input('Желаете сыграть еще раз (y - да / n - нет)? ')
    while answer.lower() not in 'y' and answer.lower() not in 'n':
        answer = input('Необходимо вводить "y" или "n"! Введите еще раз: ')
    if answer == 'y':
        return True
    else:
        return False

def play(word):
    tries = 6
    guessed_letters = []                                                        #  список уже названных букв
    guessed_words = []                                                          #  список уже названных слов
    word_completion = word[0] + '-' * (len(word) - 1)                           #  строка, содержащая символы '-' на каждую букву задуманного слова с подсказкой в виде отображения первой буквы
    counter = 0
    flag = False
    print('Давайте играть в угадайку слов!')
    print('Всего попыток -', tries)
    print(display_hangman(6))
    print('Скрытое слово:', word_completion)
    print('(', word, ')')
    
    while True:                                                                 #  бесконечный цикл на ввод текста пользователем
        text_input = input('Введите текст: ')
        
        while not text_input.isalpha():                                         #  проверка корректности вводимых данных
            text_input = input('Необходимо ввести текст! Введите текст: ')
        
        if text_input in guessed_letters or text_input in guessed_words:        #  проверка повторного ввода введенных данных
            print('Этот текст уже вводился!')
            continue
        elif len(text_input) == 1:
            guessed_letters.append(text_input)
        elif len(text_input) > 1:
            guessed_words.append(text_input)
        
        if len(text_input) == 1 and text_input.upper() in word:                 #  условие присутствия вводимых данных (побуквенно)
            counter += 1
            print('Верно', counter, 'угадано!')
            word_completion = list(word_completion)
            for i in range(len(word)):
                if text_input.upper() in word[i]:
                    word_completion[i] = text_input.upper()                     #  замена символов '-' на введенные данные 
            word_completion = ''.join(word_completion)
            print(word_completion)
        elif len(text_input) == len(word) and text_input.upper() in word:       #  условие присутствия вводимых данных (слово целиком)
            print('Поздравляем, вы угадали слово целиком! Вы победили!')
            if yes_or_no():                                                     #  предложение сыграть еще раз
                flag = True
                break
            else:
                print('До новых встреч!')
                break
        
        elif text_input.upper() not in word:                                    #  условие отсутствия вводимых данных                                  
            print('Промах!')
            tries -= 1
            print(display_hangman(tries))
            print('Осталось попыток:', tries)
            if tries == 0 and '-' in word_completion:
                print('Это провал конечно)')
                print('Загаданное слово -', word)
                if yes_or_no():
                    flag = True
                    break
                else:
                    print('До новых встреч!')
                    break
        
        if '-' not in word_completion:                                          #  условия окончания игры (все символы отгаданы)
            print('Поздравляем, вы угадали слово! Вы победили!')
            if yes_or_no():                                                     #  предложение сыграть еще раз
                flag = True
                break
            else:
                print('До новых встреч!')
                break
    return flag
    
while True:
    word = get_word()
    flag = play(word)
    if flag == True:
        continue
    else:
        break