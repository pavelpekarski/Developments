import random
print('����� ���������� � �������� ��������')
x = input('������� ������ ������� ��������� ���������� ������ �����: ')
while not x.isdigit():
    x = input('������� �����: ')
x = int(x)
n = random.randint(1, x)
print('��������� �����:', n)

def is_valid(num):
    while not num.isdigit() or int(num) not in range(1, x + 1):
        print('� ����� ���� ���-���� ������ ����� ����� �� 1 ��', x, '?')
        num = input()
    num = int(num)
    if 1 <= num <= x:
        return True, num
    else:
        return False

counter = 0
while True:
    print('������� ����� � ��������� �� 1 ��', x)
    num = input()
    counter += 1
    flag, num_valid = is_valid(num)
    if flag == True:
        num_valid = int(num_valid)
        if num_valid < n:
            print()
            print('���� ����� ������ �����������, ���������� ��� �����')
        elif num_valid > n:
            print()
            print('���� ����� ������ �����������, ���������� ��� �����')
        else:
            print()
            print('�� �������, �����������!')
            print('���������� �������:', counter)
            print('�������, ��� ������ � �������� ��������. ��� ��������...')
            print()
            s = input('������� ��� ���? (y - �� / n - ���) ')
            if s == 'y':
                x = input('������� ������ ������� ��������� ���������� ������ �����: ')
                while not x.isdigit():
                    x = input('������� �����: ')
                x = int(x)
                n = random.randint(1, x)
                print('��������� �����:', n)
                continue
            elif s == 'n':
                print('�� ����� ������!')
                break