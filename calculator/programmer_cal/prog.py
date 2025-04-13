def programmer():
    print("select the number sytem : ")
    print("1.Binary")
    print("2.Octal")
    print("3.Decimal")
    print("4.HexaDecimal")
    choose = int(input("Select one option between (1-4) : "))
    if(choose == 1):
        num1 = input("enter the value : ")
        num2 = input("enter the value : ")
        op = input("enter an opperation like add,sub,mul,div")
        if op == "add":
            sum = bin(int(num1,2) + int(num2,2))
            print(f"The sum is : {sum[2:]}")    
        elif op == "sub":
            diff = bin(int(num1,2)-int(num2,2))     
            print(f"difference = {diff[2:]}")
        elif op == "mul":
            mul = bin(int(num1,2)*int(num2,2))
            print(f"multiplication = {mul[2:]}")
        elif op == "div":
            div = bin(int(num1,2)//int(num2,2))
            print(f"Division = {div[2:]}")
    elif choose == 2:
        num1 = input("enter the value : ")
        num2 = input("enter the value : ")
        op = input("enter an opperation like add,sub,mul,div")
        if op == "add":
            sum = oct(int(num1,8) + int(num2,8))
            print(f"The sum is : {sum[2:]}")    
        elif op == "sub":
            diff = oct(int(num1,8)-int(num2,8))     
            print(f"difference = {diff[2:]}")
        elif op == "mul":
            mul = oct(int(num1,8)*int(num2,8))
            print(f"multiplication = {mul[2:]}")
        elif op == "div":
            div = oct(int(num1,8)//int(num2,8))
            print(f"Division = {div[2:]}")
    elif choose == 3:
        num1 = input("enter the value : ")
        num2 = input("enter the value : ")
        op = input("enter an opperation like add,sub,mul,div")
        if op == "add":
            sum = (int(num1) + int(num2))
            print(f"The sum is : {sum[2:]}")    
        elif op == "sub":
            diff = (int(num1)-int(num2))     
            print(f"difference = {diff[2:]}")
        elif op == "mul":
            mul = (int(num1)*int(num2))
            print(f"multiplication = {mul[2:]}")
        elif op == "div":
            div = (int(num1)//int(num2))
            print(f"Division = {div[2:]}")
    elif choose == 4:
        num1 = input("enter the value : ")
        num2 = input("enter the value : ")
        op = input("enter an opperation like add,sub,mul,div")
        if op == "add":
            sum = hex(int(num1,16) + int(num2,16))
            print(f"The sum is : {sum[2:].upper()}")    
        elif op == "sub":
            diff = bin(int(num1,16)-int(num2,16))     
            print(f"difference = {diff[2:].upper()}")
        elif op == "mul":
            mul = bin(int(num1,16)*int(num2,16))
            print(f"multiplication = {mul[2:].upper()}")
        elif op == "div":
            div = bin(int(num1,16)//int(num2,16))
            print(f"Division = {div[2:].upper()}")
    ask = input("Do You Want to continue (yes or no) : ")
    if ask == "yes":
        programmer()
    elif ask == "no":
        return 
    else :
        print("enter an valid answer")

