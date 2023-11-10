import os 


def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
def powr(num1,num2):
    return num1**num2
def mod(num1,num2):
    return num1%num2

oparation_dict = {
    '+':add,
    '-':sub,
    '*':mul,
    '/':div,
    '**':powr,
    '%':mod

}

def calculator():

    number1 = float(input("Enter First Number :"))
    for key in oparation_dict:
        print(key)

    continueflag = True
    while continueflag:

        # oparation_symbol = ''
        # def oparationsymbol():
        #     global oparation_symbol
            
        #     if oparation_symbol not in oparation_dict:
        #         print("Symbol is incorrect!")
        #         oparationsymbol()

        # oparationsymbol()
        oparation_symbol = input("Enter oparation you want..:")

        number2 = float(input('Enter Second Number :'))
        oparation = oparation_dict[oparation_symbol]
        output = oparation(number1,number2)
        print(f'The result of {number1} {oparation_symbol} {number2} is : {output}')
        continueinp = input("Enter 'Y' to continue or Enter 'N' to start new or Enter 'E' to Exit : ").lower()
        if continueinp == 'y':
            number1 = output
        elif continueinp == 'n':
            continueflag = False
            os.system('cls')
            calculator()
        elif continueinp == 'e':
            continueflag = False
            print('Exit')

calculator()