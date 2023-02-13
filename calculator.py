import os 

while True:
    print("select a number")
    print("1.addition")
    print("2.substraction")
    print("3.multiplication")
    print("4.division")
    print("5.existing")
    ch= input("enter your choice")
    if ch=='1':
        a= int(input("enter first number:"))
        b= int(input("enter second number:"))
        print(f'{a} +{b} is {a+b}')
    elif ch=='2':
        a= int(input("enter first number:"))
        b= int(input("enter second number:"))
        print(f'{a} - {b} is {a-b}')
    elif ch=='3':
        a= int(input("enter first number:"))
        b= int(input("enter second number:"))
        print(f'{a} * {b} is {a*b}')
    elif ch=='4':
        a= int(input("enter first number:"))
        b= int(input("enter second number:"))
        print(f'{a} / {b} is {a/b}')
    elif ch=='5':
        print('existing...')
        break
    else:
        print('invalid choice')
    input('press enter to continue...')
    os.system('cls')








