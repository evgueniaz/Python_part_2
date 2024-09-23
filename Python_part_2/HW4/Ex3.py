# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.


MULTIPLE_ITEM = 50
PERCENT = 0.015
PERCENT_BONUS = 0.03
MIN_LIMIT = 30
MAX_LIMIT = 600
PERCENT_RICHNESS = 0.10
RICHNESS_AMOUNT = 5_000_000
COUNT_OPERATIONS = 3
CMD_DEPOSIT = '1'
CMD_WITHDRAW = '2'
CMD_OPERATIONS = '3'
CMD_EXIT = '4'

balance = 0
operations = 0

def deposite(amount: float) -> None:
    global balance
    global operations
    balance += amount
    operations += 1

def withdraw(amount: float) -> None:
    global balance
    global operations
    commission = amount * PERCENT
    if commission < MIN_LIMIT:
        commission = MIN_LIMIT
    elif commission > MAX_LIMIT:
        commission = MAX_LIMIT

    if commission + amount > balance:
        print(f'Fonds are exceeded!')
    else:
        operations += 1
        balance -= (amount + commission)
        list_operation.append([str('Withdraw commission'), -1 * commission])
        print(f'The withdraw amount is {amount}, Commission for the withdraw is : {commission}.'
              f'The total withdrawn amount is {amount + commission}')
def bonus_operation():
    global balance
    global operations
    if operations % COUNT_OPERATIONS == 0:
        balance = balance + PERCENT_BONUS * balance
        list_operation.append([str('Bonus deposit'), PERCENT_BONUS * balance])
        print("The deposited bonus amount is : ", PERCENT_BONUS * balance)
def exit_operations():
    print("Thank you for using our banking services!\n")
    exit()
def amount_proof() -> int:
    amount = 1
    while amount % MULTIPLE_ITEM != 0:
        amount = int(input(f'Enter an amount multiple of {MULTIPLE_ITEM}:  '))
    if amount % MULTIPLE_ITEM == 0:
        return amount
def richness_proof():
    global balance
    if balance > RICHNESS_AMOUNT:
        sum_percent = balance * PERCENT_RICHNESS
        balance -= sum_percent
        list_operation.append([str('Richness tax'), -1 * sum_percent])
        print(f'The tax on richness {sum_percent} has been applied')


list_operation = []

while True:
    action = input(
        f'Deposit - {CMD_DEPOSIT}\n'
        f'Withdraw - {CMD_WITHDRAW}\n'
        f'List of operations - {CMD_OPERATIONS}\n'
        f'Exit - {CMD_EXIT}\n'
        f'Choose an action:  ')

    if action == '1' or action == '2':
        amount = amount_proof()

        if action == '1':
            deposite(amount)
            list_operation.append([str('Deposit'), amount])
            richness_proof()
        else:
            withdraw(amount)
            list_operation.append([str('Withdraw'), -1 * amount])
        bonus_operation()

        print(f'Actual balance is {balance}')

    elif action == '3':
        print(list_operation)

    elif action == '4':
        exit_operations()

    else:
        print(f"You've entered a wrong command")

