immutable_var = 13, 'слон', 4.5
print(immutable_var)
immutable_var[0] = 6  #невозможная операция, т.к. кортеж - неизменяемыйы тип данных
mutable_list = ['солнце' , 'огонь', 'цветок']
mutable_list[1] = 'картофель'
print(mutable_list)