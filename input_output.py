# 0.Ввод и вывод
# сумма трех чисел
def sum_of_three(a,b,c):
    print(a+b+c);
# площадь прямоугольника 
def area_of_rectangle(a,b):
    print(a * b);
# периметр прямоугольника
def perimeter_of_rectangle(a,b):
    print(2*(a+b));
# площадь круга
def area_of_circle(a):
    print(3.14 * a**2);
# сумма дробны чисел
def sum_of_float(a,b,c):
    print(float(a + b + c));
#задача с яблоками и школьниками
def apples_kids(apples, kids):
    each = apples // kids;
    left = apples % kids;
    print(f'каждому: {each}, остаток:{left}');