n = abs(int(input('Введите количество элементов списка А: ')))

A_entered = input("Введите через пробел элементы списка: ").split()
A_num = list(map(int, A_entered))

if len(A_num) != n:
    print('Введенные элементы не соответствуют заявленному количеству!')

else:
    x = int(input('Введите число x, которое необходимо найти в списке: '))
    count = 0
    
    for i in range(n):
        if A_num[i] == x:
            count += 1
    print(f'Число {x} встречается в списке A {count} раз') 