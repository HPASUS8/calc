math = input('Привет! Выбери действие и напиши это действие: умножение, деление, сложение и вычитание: ')
first = int(input('Хорошо... Теперь напиши первое число: '))
second = int(input('Окей... Теперь напиши второе число: '))

print('')
print(f'Выполняется {math}...')
print('')

if math.lower() == 'умножение':
    multi = first * second
    print(f'Умножение {first} на {second} равно {multi}!')

elif math.lower() == 'деление':
    div = first / second
    print(f'Деление {first} на {second} равно {div}!')

elif math.lower() == 'сложение':
    plus = first + second
    print(f'Сумма {first} и {second} равна {plus}!')

elif math.lower() == 'вычитание':
    minus = first - second
    print(f'Разность {first} и {second} равна {minus}!')

else:
    print(f'Твоё действие {math} не существует!')