p=float(input("initial amount:"))
t=float(input("time duration(in year):"))
r=float(input("intrest rate:"))
simple_intrest=(p*t*r)/100
print("simple intrest for amount",p,"for duration",t," years is",simple_intrest)
print("total amount is",p+simple_intrest)