# 1. Создайте список из 10 четных чисел и выведите его с помощью цикла for
def list_of_ten_digits():
    even_num = [i * 2 for i in range(10)];
    for num in even_num:
        print(num);

# 2. Создайте список из 5 элементов. Сделайте срез от второго индекса до четвертого
def cut_of_list(a,b,c,d,e):
    list_of_num = [a, b, c, d, e];
    slice_list = list_of_num[2:4];
    print(slice_list);

# 3. Создайте пустой список и добавьте в него 10 случайных чисел и выведите их. В данной задаче нужно использовать функцию randint. НО В ОЗУЧЕНННОМ ЗАДАНИИ БЫЛО СКАЗАНО БЕЗ ИМПОРТОВ!!!
# если использовать импорт, то код будет выглядят:
#      new_list = []
#     for n in range(10):
#         new_list.append(randint(1, 10))
#     print(new_list)
def list_with_random(a,b,c,d,e,f,g,h,k,l):
    new_list = [a,b,c,d,e,f,g,h,k,l];
    print(new_list);
    return new_list;

# 4.Удалите все элементы из списка, созданного в задании 3
def clear_new_list(empty_list):
    """Удалить все элементы из переданного списка (очистить)."""
    empty_list.clear();
    print(empty_list);

# 5.Создайте список из введенной пользователем строки и удалите из него символы 'a', 'e', 'o'
def list_of_char(new_str):
    chars = list(new_str);
    filtered = [ch for ch in chars if ch not in ('a', 'e', 'o')];
    print(filtered);

## 6.Даны два списка, удалите все элементы первого списка из второго

# a = [1, 3, 4, 5]
# b = [4, 5, 6, 7]
# # Вывод
# >>> [6, 7]

def del_first_list_from_second(list_a, list_b):
    result = list_b[:];
    for item in list_a:
        while item in result:
            result.remove(item);
    print(result);

# 7.Создайте список из случайных чисел и найдите наибольший элемент в нем. Опять же без импурта!
def max_el(lst):
    max_val = max(lst);
    print(f'Наибольший элемент: {max_val}');
    return max_val;

# 8.Найдите наименьший элемент в списке из задания 7
def min_el(lst):
    min_val = min(lst);
    print(f'Наименьший элемент:: {min_val}');
    return min_val;

# 9.Найдите сумму элементов списка из задания 7
def sum_of_list(lst):
    total = sum(lst);
    print(f'Сумма элементов: {total}');
    return total;

# 10.Найдите среднее арифметическое элементов списка из задания 7
def avr_list_num(lst):
    avg = sum(lst) / len(lst);
    print(f'Среднее арифметическое:{avg}');
    return avg