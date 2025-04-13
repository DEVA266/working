import std_cal.std_cal as std
import sci_fic_cal.scientific as sci
import programmer_cal.prog as pro
print("----Welcome----")
print("1.Standard Calculator")
print("2.Scientific Calculator")
print("3.Programmer Calculator")
c = int(input("Choose one option 1,2,3 : "))
if c==1:
    print("the operations are add,sub,mul,div,mod,float,inverse,negoate,percentage,square,sqrt,pow10,pow")
    std.standard()
elif c==2:
    sci.scientific()
elif c==3:
    pro.programmer()
else :
    print("choose an valid option")
