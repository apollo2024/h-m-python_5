# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

num = int(input())
qs = num
num_1 = int(input())
counter = 0
def qwerty (num, num_1):
    if num_1 == 1:
        return num
    return (num * qwerty(num, num_1 - 1))
print(qwerty (num, num_1))