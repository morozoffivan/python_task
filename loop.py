# 1. Вывод чисел от 0 до N
# Пользователь вводит число N. Выведите все числа от 0 до N включительно.

def int_from_zero(a):
    for i in range(a + 1):
        print(i);

# 2. Вывод чисел от K до N
# Пользователь вводит числа K и N. Выведите все числа от K до N включительно.

def int_from_zero_to_k(a, b):
    for i in range(a, b + 1):
        print(i);

# 3. Сумма от K до N
# Пользователь вводит числа K и N. Выведите сумму чисел от K до N включительно.

def sum_from_n_to_k(a,b):
    total_sum = 0;
    
    for i in range(a, b + 1):
        total_sum += i;
        
    print(total_sum);
    
# 4. Сумма четных от K до N
# Пользователь вводит числа K и N. Выведите сумму только четных чисел от K до N включительно.

def sum_of_odds(a,b):
    odd_sum = 0;
    
    for i in range(a, b + 1):
        if i % 2 == 0:
            odd_sum += i;
            
    print(odd_sum);
    
# 5. Сумма дробей (часть первая)
# Пользователь вводит число N. Найдите сумму чисел: 1 + 1.1 + 1.2 + 1.3 + ... + (1 + N / 10).

def sum_of_float(a):
    total_sum = 0.0;
    
    for i in range(a + 1):
        total_sum += 1 + (i / 10);

    print(total_sum);
    
# 6. Сумма дробей (часть вторая)
# Пользователь вводит число N. Найдите сумму чисел: 1 + 1/2 + 1/3 + ... + 1/N

def sum_of_float_2(a):
    total_sum = 0.0;
    for i in range(1, a + 1):
        total_sum += 1 / i;

    print(round(total_sum,3));
