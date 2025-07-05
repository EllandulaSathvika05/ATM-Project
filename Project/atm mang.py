print("==========WELCOME TO YONO APP==========")

acc = int(input("set your account number"))
pin = int(input("set your pin number"))

ACCOUNT_NUMBER = acc
PIN_NUMBER = pin
name = input("enter your name")

a = int(input("ENTER YOUR ACCOUNT NUMBER :"))
b = int(input("ENTER YOUR PIN NUMBER"))

if a==ACCOUNT_NUMBER and b==PIN_NUMBER:
    print('''==========LOGIN COMPLETED==========
            WELCOME SATHVIKA ELLANDULA

            1.DEPOSITE
            2.WITHDRAW
            3.BANK BALANCE
            4.MINI STATEMENT
            5.BLOCK THE DEBITCARD
            ''')
    balance = 1000000
    select = int(input("ENTER YOUR OPTION : "))
    if select == 1:
        c = int(input("ENTER YOUR DEPOSITE AMOUNT : "))
        print("YOUR TOTAL AMOUNT IS :",c+balance)
    elif select == 2:
        c = int(input("ENTER YOUR WIDTHDRAW AMOUNT : "))
        print("YOUR BALANCE IS :",balance-c)
    elif select == 3:
        c = int(input("enter your pin number"))
        if c==PIN_NUMBER:
             print("YOUR BANK BALANCE IS :",balance)
        else:print("INVALID PIN NUMBER")
        
       
    elif select == 4:
        print('''==========MINI STATEMENT==========
              ACCOUNT NUMBER : 9014680892
              PIN NUMBER     :  ****
              ACCOUNT HOLDER : ELLANDULA
              BANK BALANCE IS : 1000000''')
    elif select == 5:
        a = input("ENTER YOUR NAME : ")
        b = int(input("ENTER YOUR ACCOUNT NUMBER : "))
        c = int(input("ENTER YOUR PIN NUMBER : "))
        d = int(input("ENTER YOUR MOBILE NUMBER : "))
        e = input("REASON FOR BLOCKING DEBIRCARD : ")
        print("YOUR DEBITCARD IS BLOCK ")
        print(a)
        print(b)
        print(c)
        print(d)
else:
    print("SOMETHING WENT WRONG PLEASE TRY AGAIN")