import math

print("Welcome to The Super Calculator Version 1.5!")
Value1 = input("Please type your 1st value\n(If you wish to square root, this is the value that will be used): ")
Number1 = float(Value1)
Value2 = input("Please type your 2nd value: ")
Number2 = float(Value2)
Operator = input("Please type in the operator \n(1=add, 2=subract, 3=multiply, 4=divide, 5=Power 6=Square_Root \n7=Modulus 8=FloorDivison): ")
Op = int(Operator)
if Op == 1:
print(Number1+Number2)
elif Op == 2:
print(Number1-Number2)
elif Op == 3:
print(Number1*Number2)
elif Op == 4:
print(Number1/Number2)
elif Op == 5:
print(pow(Number1, Number2))
elif Op == 6:
print(math.sqrt(Number1))
elif Op == 7:
print(Number1 % Number2)
elif Op == 8:
print(Number1//Number2)
else:
print("Sorry, that doesn't work please try values 1 - 7 (no decimals) ")

print("Thank you for using The Super Calculator!")
