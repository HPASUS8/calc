math = input('Привет! Выбери действие и напиши это действие: умножение, деление, сложение и вычитание: ')
first = int(input('Хорошо... Теперь напиши первое число: '))
second = int(input('Окей... Теперь напиши второе число: '))

if math.lower() == 'умножение':
    multi = first * second
    print(f'Итак... Умножение {first} на {second} будет... {multi}!')

if math.lower() == 'деление':
    div = first / second
    print(f'Итак... Деление {first} на {second} будет... {div}!')

if math.lower() == 'сложение':
    plus = first + second
    print(f'Итак... Сумма {first} и {second} равна... {plus}!')

if math.lower() == 'вычитание':
    minus = first - second
    print(f'Итак... Разность {first} и {second} равна... {minus}!')
