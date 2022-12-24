#____________________________1______________________________
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# list_nums = input('nums = ').split(sep=',')
# sum = 0
# for i in range(len(list_nums)):
#     if i % 2 != 0:
#         sum += int(list_nums[i])
# print(sum)

#_____________________________2_______________________________
#Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# list_nums = input('Nums = ').split(sep=',')
# list_result = []
# for i in range(len(list_nums)):
#     if i < int((len(list_nums)/2)):
#         list_result.append(int(list_nums[i])*int(list_nums[len(list_nums)-1-i]))
#     elif len(list_nums)%2 !=0:
#          list_result.append(int(list_nums[i])*int(list_nums[i]))
#          break
# print(list_result)

#__________________________3_____________________________
#Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# list_nums = input('Введи список вещественных чисел через пробел: ').split();
# nums_list = []
# for i in range(len(nums)):
#     nums_list.append(nums[i])
# print(nums_list)
# list_nums = ['1.1', '1.2', '3.1', '5', '10.01']
# print(list_nums)
# list_drob = []
# for i in list_nums:
#     n = i.split(sep='.')
#     if len(n) == 1:
#         n.append('0')
#     list_drob.append(float(f'0.{n[1]}'))
# list_drob.remove(0.0)
# # print(list_drob)
# min_ = list_drob[0]
# max_ = list_drob[0]
# for ele in list_drob:
#     if ele > max_:
#         max_ = ele
#         # print(f'макс= {max_}')
#     if ele < min_:
#         min_ = ele
#         # print(f'min = {min_}')
# print(max_-min_)

#_________________________________________________________________
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# a = int(input('Число: '))
# list_ = []
# while a != 1:
#     if a % 2 == 1:
#         list_.append('1')
#     if a % 2 == 0:
#         list_.append('0')
#     if a//2==1:
#         list_.append('1')
#     a = a//2
# list_.reverse()
# print("".join(list_))

#____________________________________________________________________________________
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# n = int(input('n = '))
# list_fib = [0,1]
# list_negfib = [0,1]
# list_fulfib = []
# for i in range(2, n+1):
#     list_fib.append(list_fib[i-2]+list_fib[i-1])
#     list_negfib.append(list_negfib[i-2] - list_negfib[i-1])

# for i in range(len(list_negfib)-1,0,-1):
#     print(i)
#     list_fulfib.append(list_negfib[i])
# for i in list_fib:
#     list_fulfib.append(i)
# print(list_fulfib)
