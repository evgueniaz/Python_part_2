 # Напишите программу, которая получает целое число и возвращает его
 # шестнадцатеричное строковое представление. Функцию hex используйте для проверки
 # своего результата.


DIV_HEX = 16

original_num: int = int(input("Enter a whole number:  "))
num = original_num
res: str = ""
while num > 0:
    remainder = num % DIV_HEX
    if remainder == 10:
        remainder = 'A'
    if remainder == 11:
        remainder = 'B'
    if remainder == 12:
        remainder = 'C'
    if remainder == 13:
        remainder = 'D'
    if remainder == 14:
        remainder = 'E'
    if remainder == 15:
        remainder = 'F'
    res = str(remainder) + res
    num //= DIV_HEX

print(f'The number {original_num} in {DIV_HEX}-system is {res}')
