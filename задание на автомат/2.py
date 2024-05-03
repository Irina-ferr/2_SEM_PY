import numpy as np

def apply_functions(matrix_values, matrix_functions):
    # Применяем каждую функцию к соответствующему элементу матрицы значений
    result_matrix = np.vectorize(lambda f, v: f(v))(matrix_functions, matrix_values)
   
    return result_matrix

# Запрос размера матрицы у пользователя
rows = int(input('Введите количество строк: '))
cols = int(input('Введите количество столбцов: '))

# Создание матрицы значений
print('Введите числа\n')
matrix_values = np.empty((rows, cols), dtype=np.float64)
for i in range(rows):
    for j in range(cols):
        matrix_values[i][j] = float(input(f'a[{i}][{j}] = '))

# Создание матрицы функций с помощью словаря
dictionary = {'sin(x)': np.sin, 'cos(x)': np.cos, 'str(x)': np.str_, 'x^2': lambda x: x**2, '[x]': np.abs, 'tg(x)' :np.tan, 'ln(x)': np.log, 'sqr(x)':np.sqrt, 'x+1': lambda x: x + 1}
print('Введите функции\n В формате sin(x) cos(x) tg(x) ln(x) sqr(x) x^2 [x] str(x) x+1')
matrix_functions = np.empty((rows, cols), dtype=object)
for i in range(rows):
    for j in range(cols):
        function_str = input(f'f(a[{i}][{j}]) = ')
        matrix_functions[i][j] = dictionary[function_str]

result = apply_functions(matrix_values, matrix_functions)
print(result)