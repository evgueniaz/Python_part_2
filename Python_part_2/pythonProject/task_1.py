# text = input('Enter something: ')
# if text.isdecimal():
#     print(int(text), bin(int(text)), oct(int(text)),hex(int(text)))
# else:
#     print('your text is written in ASCII' if text.isascii() else 'your text is not written in ASCII')
#


# BIG_LEAP_YEAR = 400
# LARGE_NOT_LEAP_YEAR = 100
# SMALL_LEAP_YEAR = 4
# MULTIPLE = 0
# ORIGIN = 1582
#
# year = int(input("Enter a year: "))
# if year < ORIGIN:
#     result = "This year is before the Gregorian calender was accepted!"
# elif year % BIG_LEAP_YEAR == 0:
#     result = "The year is leap"
# elif year % LARGE_NOT_LEAP_YEAR == 0:
#     result = "The year is not leap"
# elif year % SMALL_LEAP_YEAR == 0:
#     result = "The year is leap"
# else:
#     result = "The year is not leap"
# print(result)


# LOWER_LIMIT = 1
# UPPER_LIMIT = 999
# ONE = 1
# TEN = 10
# HUNDRED = 100
#
# num = LOWER_LIMIT - ONE
# while num < LOWER_LIMIT or num > UPPER_LIMIT:
#     num = int(input("Enter a number between 1 and 999: "))
#     # print("Your number is out of the indicated interval!")
# if num < TEN:
#     result = num ** 2
#     # print(f"Your number squared is : {num ** 2}")
# elif num < HUNDRED:
#     result = (num // TEN) * (num % TEN)
#     # print(f'Product of the digits of your number is: {(num // TEN) * (num % TEN)}')
# else:
#     d1 = num // HUNDRED
#     d2 = num // TEN % TEN
#     d3 = num % HUNDRED % TEN
#     result = d3 * HUNDRED + d2 * TEN + d1
#     # print(f'Your number when reverted is: {d3 * HUNDRED + d2 * TEN + d1}')
# print(result)


# LOWER_LIMIT = 2
# UPPER_LIMIT = 10
# COLUMN = 4
# for i in (LOWER_LIMIT, LOWER_LIMIT + COLUMN):
#     for j in range(LOWER_LIMIT, UPPER_LIMIT):
#         for k in range(i, i + COLUMN):
#             print(f'{k: >2} x {j: >2} = {i * j: >2}', end= '\t')
#         print()
#     print()


SPACE = ' '
STAR = '*'
ONE = 1

rows = int(input('Enter a number of rows in the tree: '))
spaces = rows - ONE
stars = ONE

for i in range(rows):
    print(spaces * SPACE + stars * STAR)
    stars += 2
    spaces -= 1




