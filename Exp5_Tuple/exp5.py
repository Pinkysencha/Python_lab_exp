#tuple 
def calc(a,b):
    return (a+b, a-b,a*b, a/b)
a = int(input("\n\nEnter a : "))
b = int(input("Enter b : "))

result = calc(a,b)
print("Addition: ",result[0])
print("Subtraction: ",result[1])
print("Multiplication: ",result[2])
print("Divison: ",result[3])
