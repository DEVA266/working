def standard():
    import math
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a//b
    def modd(a,b):
        return a%b
    def float_div(a,b):
        return a/b
    def inverse(a):
        return 1/a
    def negotate(a):
        return (-1*a)
    def percentage(a,b):
        # a refers to the value of the number 
        # b refers to the percentage 
        # b should be less than or equal to 100
        if b<=100:
            return (a*(b/100))
    def square(a):
        return a**2
    def sqrt(a):
        return math.sqrt(a)
    def pow10(a):
        return a**10
    def pow(a,b):
        # a is a base value
        # b should be the power value
        return a**b
    choice = input("Do you want to continue (yes or no) : ")
    if choice == "yes":
        standard()
    elif choice == "no":
        return 
    else :
        print("enter an valid answer")



