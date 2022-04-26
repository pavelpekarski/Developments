import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

def is_valid(num):
    while not num.isdigit():
        num = input('���������� ������ �����: ')
    num = int(num)
    return num

def valid_answer(s):
    while s.lower() not in 'y' and s.lower() not in 'n':
        print('���������� ������ "y" ��� "n"!')
        s = input()
    return s

def generate_password(length, chars):
    x = random.sample(chars, length)
    x = ''.join(x)
    return x

print('������� ���������� ������������ �������: ')
c = input()
count = is_valid(c)

print('������� ����� ������: ')
l = input()
length = is_valid(l)

print('�������� �� ����� 0123456789? (y - �� / n - ���): ')
q_1 = input()
question_1 = valid_answer(q_1)

print('�������� �� ��������� ����� ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y - �� / n - ���): ')
q_2 = input()
question_2 = valid_answer(q_2)

print('�������� �� �������� ����� abcdefghijklmnopqrstuvwxyz? (y - �� / n - ���): ')
q_3 = input()
question_3 = valid_answer(q_3)

print('�������� �� ������� !#$%&*+-=?@^_? (y - �� / n - ���): ')
q_4 = input()
question_4 = valid_answer(q_4)

print('��������� �� ������������� ������� il1Lo0O? (y - �� / n - ���): ')
q_5 = input()
question_5 = valid_answer(q_5)

if question_1 == 'y':
    chars += digits
if question_2 == 'y':
    chars += uppercase_letters
if question_3 == 'y':
    chars += lowercase_letters
if question_4 == 'y':
    chars += punctuation

if question_5 == 'y':
    s = list(chars)
    chars_new = []
    for i in range(len(s)):
        if s[i] not in 'il1Lo0O':
            chars_new.append(s[i])
    chars = ''.join(chars_new)
            
for _ in range(count):
    print(generate_password(length, chars))