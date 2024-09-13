# Напишите код, который запрашивает число и сообщает является ли оно простым
# или составным. Используйте правило для проверки: “Число является простым,
# если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод
# отрицательных чисел и чисел больше 100 тысяч.

LOWER_LIMIT = 1
UPPER_LIMIT = 999
ONE = 1


num = LOWER_LIMIT - ONE
while num < LOWER_LIMIT or num > UPPER_LIMIT:
    num = int(input("Enter a number between 1 and 100000: "))
    # print("Your number is out of the indicated interval!")
status = 'Your number is prime.'
if num == 1:
    print('Your number is neither prime nor compound.')
else:
    for i in range(LOWER_LIMIT + ONE, int(num / 2 + 1)):
        if num % i == 0:
            status = 'Your number is compound.'
            print(status)
            break
    if status != 'Your number is compound.':
        print(status)

