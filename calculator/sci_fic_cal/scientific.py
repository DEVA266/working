def scientific():
    import math
    pi = 3.14159265359
    e = 2.718281828459045
    def sin(a):
        return math.sin(math.radian(a))
    def cos(a):
        return math.cos(math.radian(a))
    def tan(a):
        return math.tan(math.radian(a))
    def factorial(a):
        return math.factorial(a)
    def exp(a,b):
        # a to be the base value
        # b to be the power value
        return a*(10**b)
    def mod(a,b):
        return a%b
    def square(a):
        return a*a
    def sqrt(a):
        return math.sqrt(a)
    def pows(a,b):
        return a**b
    def base10(a):
        return 10**a
    def log(a):
        return math.log(a)
    def inverse(a):
        return 1/a
    def pow3(a):
        return a**3
    def cube_root(a):
        return math.cbrt(a)
    def pow_root(a,b):
        # a refers to the base value and b refers to the power of the root value
        return a**(1//b)
    def two_pow(a):
        return 2**a
    def log_base(a,b):
        # a refers to number and b refers to the base 
        return math.log(a,b)
    def exponential(a):
        return e**a


