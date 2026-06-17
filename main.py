# 0.Ввод и вывод
import input_output as task_1

task_1.sum_of_three(1,2,3);
task_1.area_of_rectangle(3,5);
task_1.perimeter_of_rectangle(5,4);
task_1.area_of_circle(5);
task_1.sum_of_float(12.57,2.3,3.57567);
task_1.apples_kids(10,3);

# 1.Операторы
import operators as task_2

task_2.odd_or_not(2,10);
task_2.one_positive(0,1,-2);
task_2.last_digit(1223);
task_2.sum_of_two_digits(99);
task_2.sum_of_three_digits(332);
task_2.three_digits_different(123);
task_2.clock(1000);

# 2.Условный оператор
import conditional_operator as task_3

task_3.min_max_of_two(10,10);
task_3.four_digits_or_not(1234);
task_3.is_it_triangle(3,4,5);
task_3.what_period_of_day(22);
task_3.what_day_is_today(7);
task_3.what_kind_of_int(-12.5);
task_3.hourse_move(1,1,2,2);

# 3.Цикл for
import loop as task_4

task_4.int_from_zero(4);
task_4.int_from_zero_to_k(2,7);
task_4.sum_from_n_to_k(1,5);
task_4.sum_of_odds(1,5);
task_4.sum_of_float(5);
task_4.sum_of_float_2(5);

# 4.Цикл while
import loop_while as task_5

task_5.print_odd_digits(10,1);
task_5.print_digits_dev_on_three(1,15);
task_5.sum_digits_inputs_until_zero(1, 15, 10, 11, 2, 0);
task_5.max_digits_inputs_until_zero(1, 15, 10, 11, 2, 0);
task_5.min_digits_inputs_until_zero(1, 15, 10, 11, 2, 0);
task_5.factorial(3);
task_5.print_fibonacci_number(10);

# 5.Списки

import list_task as task_6
test_list = [42, 17, 89, 3, 25, 67, 11, 53, 98, 34];

task_6.list_of_ten_digits();
task_6.cut_of_list(10,20,20,30,40);
new_list = task_6.list_with_random(1,2,3,4,5,6,7,8,9,10);
task_6.clear_new_list(new_list);
task_6.list_of_char('Hello, world!');
task_6.del_first_list_from_second([1, 3, 4, 5], [4, 5, 6, 7]);
task_6.max_el(test_list);
task_6.min_el(test_list);
task_6.sum_of_list(test_list);
task_6.avr_list_num(test_list);

# 6.Функции

import function as task_7

task_7.area(4);
task_7.dev_on_three(2);
task_7.max_num_fo_list([1,2,6,3,4,5]);
task_7.count_of_even([1, 10, 2, 4, 6, 8,3,9,11]);
task_7.unique_num([1, 1, 2, 1, 3, 2, 3]);
