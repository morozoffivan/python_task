# 1. Фрукты
# Пользователь вводит число K - количество фруктов. Затем он вводит K фруктов в формате: название фрукта и его количество. Добавьте все фрукты в словарь, где название фрукта - это ключ, а количество - значение.

def fruits (fruit_1, count_1, fruit_2,count_2, fruit_3,count_3):
    dict_of_fruits = {fruit_1: count_1, fruit_2: count_2, fruit_3: count_3};
    print(dict_of_fruits);
    
# 2. Старший и младший
# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей. Создайте список friends и добавьте в него N словарей с ключами name и age. Найдите самого младшего из друзей и выведите его имя.

def friends (name_1, age_1, name_2, age_2, name_3, age_3):
    dict_of_friends = {name_1: age_1, name_2: age_2, name_3: age_3};
    min_age = min(dict_of_friends, key=dict_of_friends.get);
    print(min_age);
    
# 3. Еще немного о друзьях
# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей. Создайте список friends и добавьте в него N словарей с ключами name и age. Выведите средний возраст всех друзей и самое длинное имя.    

def friends_avr(name_1, age_1, name_2, age_2, name_3, age_3):
    dict_of_friends = {name_1: age_1, name_2: age_2, name_3: age_3};
    
    ages = dict_of_friends.values();
    average_age = sum(ages) / len(ages);

    longest_name = max(dict_of_friends.keys(), key=len);

    print(average_age);
    print(longest_name);
    
# 4. Английский словарь
# "Пора учить английский язык", - сказал себе Степа и решил написать программу для изучения английского языка. Программа получает на вход слово на английском языке и несколько его переводов на русском языке. Составьте словарь, в котором ключ - это английское слово, а значение - это список русских слов. В этой задаче нужно использовать строчный метод split().

def make_english_dict(en_word, ru_translations_str):
    translations_list = ru_translations_str.split(', ');
    
    english_dict = {en_word: translations_list};
    
    print(english_dict);