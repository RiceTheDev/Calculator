import os
import time
import sys

# a calculator. obviously, do not use it.

def plus():
    os.system('cls')
    print('Please enter the first number in the expression.\n')
    firstnmbr = int(input())
    time.sleep(0.3)
    os.system('cls')
    print('Please enter the second number in the expression.\n')
    secontnmbr = int(input())
    time.sleep(0.3)
    os.system('cls')
    print('The answer is', firstnmbr + secontnmbr)
    sys.exit()

def minus():
    os.system('cls')
    print('Please enter the first number in the expression.\n')
    firstnmbr = int(input())
    time.sleep(0.3)
    os.system('cls')
    print('Please enter the second number in the expression.\n')
    secontnmbr = int(input())
    time.sleep(0.3)
    os.system('cls')
    print('The answer is', firstnmbr - secontnmbr)
    sys.exit()
    

def multiply():
    os.system('cls')
    print('Please enter the first number in the expression.\n')
    firstnmbr = int(input())
    time.sleep(0.3)
    os.system('cls')
    print('Please enter the second number in the expression.\n')
    secontnmbr = int(input())
    time.sleep(0.3)
    os.system('cls')
    print('The answer is', firstnmbr * secontnmbr)
    sys.exit()

def divide():
    os.system('cls')
    print('Please enter the first number in the expression.\n')
    firstnmbr = int(input())
    time.sleep(0.3)
    os.system('cls')
    print('Please enter the second number in the expression.\n')
    secontnmbr = int(input())
    time.sleep(0.3)
    os.system('cls')
    if secontnmbr != 0:
        print('The answer is', firstnmbr - secontnmbr)
    else:
        print('Error: Division by zero.')
        sys.exit()

def menu():
    print('Choose a operator:')
    print('\n+ = Plus\n- = Minus\n* = Multiply\n/ = Divide\nExit = Quit\n')
    operator = input('Operator: ')
    if operator == '+':
        plus()
    if operator == '-':
        minus()
    if operator == '*':
        multiply()
    if operator == '/':
        divide()
    if operator == '':
        print('Unknown Operator.')
    if operator == 'exit' or 'Exit':
        print('Exiting...')
        time.sleep(3)
        sys.exit()
        
menu()
