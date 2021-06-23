#ATM APP
account1 = {
    'name': 'Brad',
    'accountNumber': '12345678',
    'balance': 3000,
    'overdraft': 2000
}
account2 = {
    'name': 'Kate',
    'accountNumber': '32145678',
    'balance': 3000,
    'overdraft': 2000
}

def withdraw(account, amount):
    print(f"Welcome {account['name']}")

    if account['balance'] >= amount:
        print('You can take your money')
    else:
        total = account['balance']+account['overdraft']
        if total >= amount:
            useoverdraft = input('Do you want use overdarft?  y/n')
            if useoverdraft == 'y':
                print('You can get money')
            if useoverdraft == 'n':
                print(f"{account['accountNumber']} is available just {account['balance']}")
        else:
            print("You don't have enough balance in your account")

withdraw(account1, 15000)