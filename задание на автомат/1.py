import numpy as np

def apply_functions(matrix_values, matrix_functions):
    # Применяем каждую функцию к соответствующему элементу матрицы значений
    result_matrix = np.vectorize(lambda f, v: f(v))(matrix_functions, matrix_values)
   
    return result_matrix

# Реализация запроса ЧИСЛОВОЙ МАТРИЦЫ
print('Эта программа может вычислить значения 4 функций\n')
print('Введите 4 числа\n')
a00 = int(input('a[0][0] = '))
a01 = int(input('a[0][1] = '))
a10 = int(input('a[1][0] = '))
a11 = int(input('a[1][1] = '))

matrix_values = np.array([[a00, a01], [a10, a11]], dtype=np.float64)

# Реализация запроса функций с помощью словаря
dictionary = {'sin(x)': np.sin, 'cos(x)': np.cos, 'x^2': lambda x: x**2, '[x]': np.abs, 'tg(x)': np.tan, 'ln(x)': np.log, 'sqr(x)': np.sqrt, 'str(x)': np.str_, 'x+1': lambda x: x + 1}
print('Введите 4 функции\n В формате sin(x) cos(x) tg(x) ln(x) sqr(x) x^2 [x] str(x) ')
f00 = input('f(a[0][0]) = ')
f01 = input('f(a[0][1]) = ')
f10 = input('f(a[1][0]) = ')
f11 = input('f(a[1][1]) = ')

if f00 not in dictionary or f01 not in dictionary or f10 not in dictionary or f11 not in dictionary:
    print("Ошибка: Некорректная функция")
else:
    matrix_functions = np.array([[dictionary[f00], dictionary[f01]], [dictionary[f10], dictionary[f11]]])
    result = apply_functions(matrix_values, matrix_functions)
    print(result)