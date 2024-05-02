from sympy import *
import sys


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __lt__(self, other):
        if isinstance(other, Point):
            return (self.x, self.y) < (other.x, other.y)
        raise NotImplementedError("Ошибка")

    def __gt__(self, other):
        if isinstance(other, Point):
            return (self.x, self.y) > (other.x, other.y)
        raise NotImplementedError("Ошибка")

    def __le__(self, other):
        if isinstance(other, Point):
            return (self.x, self.y) <= (other.x, other.y)
        raise NotImplementedError("Ошибка")

    def __ge__(self, other):
        if isinstance(other, Point):
            return (self.x, self.y) >= (other.x, other.y)
        raise NotImplementedError("Ошибка")

    def absolute(self):
        return Point(abs(self.x), abs(self.y))

    def round_point(self):
        return Point(float(round(self.x, 3)), float(round(self.y, 3)))


x1, x2 = symbols('x1, x2')
l = Symbol('l')

#коэффициенты целевой функции
a, b, c, d, e = 1, 2, -2, 8, -18

#коэффициенты х0
x0 = Point(1, 1)

#целевая функция
func = a * x1 ** 2 + b * x2 ** 2 + c * x1 * x2 + d * x1 + e * x2

# Частные производные
diff_func = Point(2 * a * x1 + c * x2 + d, 2 * b * x2 + c * x1 + e)
# print("Диф функция:", diff_func)


restriction_1 = -x1 + x2 <= 3
restriction_2 = x1 <= 2
restriction_3 = x2 >= 0
restriction_4 = x1 >= 0

count = 0
eps = 10 ** -5
epsilon_point = Point(eps, eps)
max_iterations = 100

while True:
    count += 1
    # print("ИТЕРАЦИЯ - ", count)

    #Градиент функции в точке x0(p, f)
    diff_func_x0 = Point(diff_func.x.subs({x1: x0.x, x2: x0.y}), diff_func.y.subs({x1: x0.x, x2: x0.y}))
    #print("Градиент функции в начальной функции:", diff_func_x0)

    if diff_func_x0.absolute() < epsilon_point:
        print("Количество итераций:", count)
        print("(x1, x2) =", x0.round_point())
        print("F(x1, x2) =", float(func.subs({x1: x0.round_point().x, x2: x0.round_point().y})))
        sys.exit()

    #Предполагаемая следующая точка c лямбда
    expected_next_point = Point(x0.x - diff_func_x0.x * l, x0.y - diff_func_x0.y * l)
    # print("Предполагаемая следующая точка:", expected_next_point)

    #Вычислим лямбду
    lamda = solve(Eq(diff(func.subs({x1: expected_next_point.x, x2: expected_next_point.y})).evalf(), 0))[0]
    # print("Шаг:", lamda)

    # Следующая точка
    next_iteration_point = Point((x0.x + lamda * (-diff_func_x0.x.evalf())).evalf(),
                                 (x0.y + lamda * (-diff_func_x0.y.evalf())).evalf())
    # print("Следующая точка:", next_iteration_point)

    # if not (restriction_1.subs({x1: next_iteration_point.x, x2: next_iteration_point.y}) and
    #         restriction_2.subs({x1: next_iteration_point.x, x2: next_iteration_point.y}) and
    #         restriction_3.subs({x1: next_iteration_point.x, x2: next_iteration_point.y}) and
    #         restriction_4.subs({x1: next_iteration_point.x, x2: next_iteration_point.y})):
    #     # Если хотя бы одно ограничение не выполняется, пропускаем эту итерацию
    #     continue
    x0 = next_iteration_point

    if count >= max_iterations:
        print("Превышено максимальное количество итераций.")
        sys.exit()
