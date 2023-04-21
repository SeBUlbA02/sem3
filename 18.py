n = abs(int(input('Введите количество элементов списка А: ')))
A_entered = input("Введите через пробел элементы списка: ").split()
A_num = list(map(int, A_entered))

if len(A_num) != n or n == 0:
    print('Введенные элементы не соответствуют заявленному количеству!')

else:
    x = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
    min = abs(x - A_num[0])
    index = 0
    
    for i in range(1, n):
        count = abs(x - A_num[i])
        if count < min:
            min = count
            index = i
    print(f'Число {A_num[index]} в списке A наиболее близко по величине к числу {x}, их разница составляет {abs(x - A_num[index])}')