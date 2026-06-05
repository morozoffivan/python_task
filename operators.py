# 1. Операторы

#1.Одинаковая четность
#Даны два целых числа: A, B. Проверить истинность высказывания: "Числа A и B имеют одинаковую четность".

def odd_or_not(a, b):
    if (a%2==0) == (b%2==0):
        print(True);
    else:
        print(False);
        
#2.Одно положительное
#Даны три целых числа: A, B, C. Проверить истинность высказывания: "Хотя бы одно из чисел A, B, C положительное".

def one_positive(a,b,c):
    if(a>0 or b>0 or c>0):
        print(True);
    else:
        print(False);
        


#3.Последняя цифра
#Дано натуральное число. Выведите его последнюю цифру.

def last_digit(a):
    print(str(a)[-1]);
    
#4.Цифры двузначного
#Дано двузначное число. Найдите сумму его цифр.

def sum_of_two_digits(a):
    b = str(a)[0];
    c = str(a)[1];
    num = int(b) + int(c);
    print(num);
    
# 5. Цифры трехзначного
# Дано трехзначное число. Найдите сумму его цифр.

def sum_of_three_digits(a):
    b = str(a)[0];
    c = str(a)[1];
    d = str(a)[2];
    num = int(b) + int(c) + int(d);
    print(num);
    
# 6. Разные цифры
# Дано трехзначное число. Проверить истинность высказывания: "Все цифры данного числа различны".

def three_digits_different(a):
    b = str(a)[0];
    c = str(a)[1];
    d = str(a)[2];
    
    if(b == c or b == d or c == d):
        print(False);
    else:
        print(True);
        
# 7. Часы (финальный босс)
# С начала суток прошло N секунд (N - целое). Найти количество часов, минут и секунд на электронных часах.

def clock(a):
    # 86400 - кол-во сек в одном дне
    seconds_in_one_day = a % 86400;
    hours = seconds_in_one_day // 3600;
    minutes = (seconds_in_one_day % 3600) // 60;
    seconds = seconds_in_one_day % 60;
    print(f'{hours:02d}:{minutes:02d}:{seconds:02d}');