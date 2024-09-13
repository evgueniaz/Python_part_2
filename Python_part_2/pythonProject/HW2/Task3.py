# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и
# знаменателем. Программа должна возвращать сумму и произведение* дробей. Для проверки
# своего кода используйте модуль fractions


import math
from fractions import Fraction

frac_1 = input("Enter a fraction of the form 'a/b':  ")
frac_2 = input("Enter another fraction of the form 'a/b':  ")
num_1 = int(frac_1.split('/')[0])
num_2 = int(frac_2.split('/')[0])
denom_1 = int(frac_1.split('/')[1])
denom_2 = int(frac_2.split('/')[1])
sum_num = num_1 * denom_2 + num_2 * denom_1
sum_denom = denom_1 * denom_2
sum_gcd = math.gcd(sum_num, sum_denom)
sum_num = int(sum_num / sum_gcd)
sum_denom = int(sum_denom / sum_gcd)

product_num = num_1 * num_2
product_denom = denom_1 * denom_2
product_gcd = math.gcd(product_num, product_denom)
product_num = int(product_num / product_gcd)
product_denom = int(product_denom / product_gcd)

print(f'The sum of {frac_1} and {frac_2} is {sum_num}/{sum_denom}')
print(f'The product of {frac_1} and {frac_2} is {product_num}/{product_denom}')

sum_fr = Fraction(num_1, denom_1) + Fraction(num_2, denom_2)
product_fr = Fraction(num_1, denom_1) * Fraction(num_2, denom_2)
print(sum_fr)
print(product_fr)
