# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)


from random import randint


LOWER_LIMIT = 0
UPPER_LIMIT = 1000

target = randint(LOWER_LIMIT, UPPER_LIMIT)

for i in range(10):
    num = int(input("Enter a number between 1 and 1000 to guess the target number: "))
    if target == num:
        print(f'You have guessed! Your number is {target}')
        break
    elif target > num:
        if i != 9:
            print('The target number is greater than yours. Try again!')
        else:
            print("The target number is greater than yours. You've spent all of the 10 attempts.")
    else:
        if i != 9:
            print('The target number is smaller than yours. Try again!')
        else:
            print("The target number is smaller than yours. You've spent all of the 10 attempts.")

print(f'The target number was {target}')