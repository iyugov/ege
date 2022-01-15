
import itertools

# Решатель задания:
# "Определение порядка переменных в таблице истинности"


# Логические переменные
variables = 'xyz'

# Логическое выражение
expression = 'neg (y -> x) and neg (x and z)'

# Шаблон таблицы истинности
pattern = (
            ('00 ', '1'),
            ('1  ', '1')
          )
          
# Изменение логического выражения на случай,
# если оно вставлено из редактора формул
expression = expression.replace('neg','not')
expression = expression.replace('->','<=')
expression = expression.replace('oplus','xor')
expression = expression.replace('equiv','==')

for line in pattern:
    print(line[0], line[1])
print('-' * 10)
# Перебор перестановок переменных
k = 0
for p_variables in itertools.permutations(variables):
    # Формирование таблицы истинности
    truth_table = []
    for i in range(1 << len(p_variables)):
        vars_line = ""
        # Формирование строки таблицы истинности
        for j in range(len(p_variables)):
            value = i & (1 << j) > 0
            vars_line += '1' if value else '0'
            locals()[p_variables[j]] = value
        f_value = eval(expression)
        f_line = '1' if f_value else '0'
        truth_table.append((vars_line, f_line))
    # Проверка соответствия таблицы истинности шаблону
    match = False
    for a_lines in itertools.permutations(truth_table, len(pattern)):
        lines_match = True
        temp_lines = []
        # Тут проверить строку на соответствие шаблону
        for i in range(len(pattern)):
            if a_lines[i][1] != pattern[i][1]:
                lines_match = False
                break
            for j in range(len(p_variables)):
                if (pattern[i][0][j] in '01') and a_lines[i][0][j] != pattern[i][0][j]:
                    lines_match = False
                    break
            if lines_match:
                temp_lines.append(a_lines[i])
        if lines_match:
            match = True
            break
    if match:
        print(''.join(p_variables))
        for line in temp_lines:
            print(line[0], line[1])
        print('-' * 10)
        k += 1
print(f'Решений: {k}')
