import random
db = {2038753667: ['Mike', 'Joe', 'mikejoe@gmail.com','pass',3000]}


def init():

    print('Welcome to ROOKIE BANK PLC')

    haveAccount = int(input('Do you have an account 1. Yes 2. No \n'))

    if haveAccount == 1:
        login()

    elif haveAccount == 2:
        register()

    else:
        print('Invalid option selected')
        init()


def login():

    print('****Login****')

    UserAccountNumber = int(input('Enter your account number\n'))
    password = input('Enter your password\n')

    for accountNumber, userDetails in db.items():
        if accountNumber == UserAccountNumber and userDetails[3] == password:
            bankOperation(userDetails)

    print('Invalid details')
    login()


def register():
    print('******Register******')
    email = input('What is your email \n')
    firstname = input('What is your first name \n')
    lastname = input('What is your last name \n')
    password = input('Create a password \n')
    accountBal = 0

    accountNumber = generateAccountNo()

    db[accountNumber] = [firstname, lastname, email, password, accountBal]

    print(f'Your Account has been created and your account number is: {accountNumber}')
    login()


def generateAccountNo():
    print('Generating account number')
    return random.randrange(1111111111, 9999999999)


def bankOperation(user):

    print(f'Welcome {user[1]} {user[0]}')

    selectedOption = int(input(
        'What will you like to do? (1) Check Balance (2) Withdraw (3) Deposit (4) Transfer (5) Logout (6) exit \n'))

    if selectedOption == 1:
        checkBal(user)

    if selectedOption == 2:
        withdrawalOperation(user)

    elif selectedOption == 3:
        depositOperation(user)

    elif selectedOption == 4:
        transfer(user)

    elif selectedOption == 5:
        logout()

    elif selectedOption == 6:
        print('Thanks for banking with us')
        exit()

    else:
        print('Invalid option selected')
        bankOperation(user)


def withdrawalOperation(user):
    print('******withdrawal******')
    withdrawAmount = int(input('How much would you like to withdraw?\n'))
    if user[4] >= withdrawAmount:
        user[4] -= withdrawAmount
        print(f'You withdrew {withdrawAmount}')
        continueTransaction(user)

    else:
        print('Insufficient fund')


def depositOperation(user):
    print('****Deposit******')
    depositAmount = int(input('How much would you like to deposit?\n'))
    user[4] += depositAmount
    print(f'You deposited {depositAmount}')
    continueTransaction(user)


def transfer(user):
    print('******withdrawal******')
    transferedAmount = int(input('How much would you like to transfer?\n'))
    if user[4] >= transferedAmount:
        user[4] -= transferedAmount
        print(f'You transferred {transferedAmount}')
        continueTransaction(user)
    else:
        print('Insufficient fund')


def logout():
    login()

def continueTransaction(user):
    selectedOption = int(input('Do you want to perform another transaction? (1) Yes (2) No \n'))
    if selectedOption == 1:
        bankOperation(user)

    elif selectedOption == 2:
        print('Thanks for banking with us')
        exit()

    else:
        print('Invalid option selected')

def checkBal(user):
    print(f'Your account balance is: #{user[4]}')
    continueTransaction(user)


init()
