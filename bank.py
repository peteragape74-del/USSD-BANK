#USSD BANKING SYSTEM CODE
#**PIN for transactions is 4589**

import time
import random
max_attempt = 3
names = random.choice(['Adam Williams','Osazu Godspower','Godfery Lucky Ekomakpaze'])
printss = ['UNION BANK', 'loading options.....']
for prints in printss:
    print(prints)
time.sleep(2)
Balance = 100000.00
networks = ['1. MTN', '2. GLO', '3. AIRTEL']
banks = ['1. Zenith bank', '2. First bank', '3. IBTC bank', '4. Union bank', '5. Access bank']

another_transaction = 'yes'
while another_transaction == 'yes':
    pin = ' '
    attempt = 0
    options = ['1. Transfer', '2. Withdraw', '3. Check Balance', '4. Airtime']
    for option in options:
        print(option)
    option = int(input('Select option by its number: '))
    if option == 1:
        acc_num = int(input('Enter account number: '))
        print('loading banks.....')
        time.sleep(1)
        for bank in banks:
            print(bank)
        bank = int(input('Select bank by its number: '))
        time.sleep(1)
        print(names)
        time.sleep(1)
        amount = int(input('Enter amount: '))
        time.sleep(1)
        if amount >= 10000:
            print('insufficient funds')
        elif amount >= 100 and amount <= 9990:
            while pin != '4589' and attempt < max_attempt:
                pin = input('Enter your pin: ')
                attempt += 1
                if pin != '4589' and attempt < max_attempt:
                    print('incorrect pin')
                    print('Try again',max_attempt - attempt,'attempt left')
                elif pin == '4589':
                    print('Transfer successful')
                    print('Your current balance is #',Balance - amount)
                    break
                else:
                    print('Reached attempt limit. ACCOUNT BLOCKED')
                    print('Visit the nearest Union bank branch to reactivate your account')
                    break
        else:
            print('amount must be #100 or above')
    elif option == 2:
        amount1 = int(input('Enter the amount you want to withdraw: '))
        time.sleep(1)
        if amount1 >= 10000:
            print('insufficient funds')
        elif amount1 >= 100 and amount1 <= 9990:
            while pin != '4589' and attempt < max_attempt:
                pin = input('Enter your pin: ')
                attempt += 1
                if pin != '4589' and attempt < max_attempt:
                    print('incorrect pin')
                    print('Try again',max_attempt - attempt,'attempt left')
                elif pin == '4589':
                    print('Withdraw successful')
                    print('Your current balance is #',Balance - amount1)
                    break
                else:
                    print('Reached attempt limit. ACCOUNT BLOCKED')
                    print('Visit the nearest Union bank branch to reactivate your account')
                    break
    elif option == 3:
        print('Your balanace is #',Balance)
    elif option == 4:
        number = int(input('Enter phone number: '))
        for network in networks:
            print(network)
        network = int(input('Select network by its number(e.g 1, 2...): '))
        if network == 1 or network == 2 or network == 3:
            amount2 = int(input('Enter amount: '))
            if amount2 >= 10000:
                print('insufficient funds')
                break
            elif amount2 >= 100 and amount2 <= 9990:
                while pin != '4589' and attempt < max_attempt:
                    pin = input('Enter your pin: ')
                    attempt += 1
                    if pin != '4589' and attempt < max_attempt:
                        print('incorrect pin')
                        print('Try again',max_attempt - attempt,'attempt left')
                    elif pin == '4589':
                        print('Airtime of',amount2,'successful')
                        print('Your current balance is #',Balance - amount2)
                        break
                    else:
                        print('Reached attempt limit. Try again after 24 hours')
                        break
    else:
        print('Invalid option. Please choose 1, 2, 3, or 4.')
        continue

    another_transaction = input('Do you want to perform another transaction? (yes/no): ').lower()

print('Thanks for banking with us!')
