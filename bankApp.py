import random
db = {}

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

    accountNumber = generateAccountNo()

    db[accountNumber] = [firstname, lastname, email, password]
    
    print(f'Your Account has been created and your account number is: {accountNumber}')
    login()


def generateAccountNo():
    print('Generating account number')
    return random.randrange(1111111111,9999999999)


def bankOperation(user):

    print(f'Welcome {user[1]} {user[0]}')

    selectedOption = int(input('What will you like to do? (1) Withdraw (2) Deposit (3) Logout (4) exit \n'))

    if selectedOption == 1:
        withdrawalOperation()

    elif selectedOption == 2:
        DepositOperation()

    elif selectedOption == 3:
        logout()

    elif selectedOption == 4:
        exit()

    else:
        print('Invalid option selected')
        bankOperation(user)


def withdrawalOperation():
    print('withdrawal')

def DepositOperation():
    print('deposit')

def logout():
    login()

init() 
