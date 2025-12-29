def addition(a,b):
    sum = a + b
    return sum

def subtraction(a,b):
    sub = a - b
    return sub

def multiplication(a,b):
    mul = a* b
    return mul

def division(a,b):
    if b == 0 :
     print("Divisor zero not allowed")
    else:
      div = a / b
      return div
 
def calculate(operand1,operand2,operation):
 return operation(operand1,operand2)
    
n1=int(input("Enter the number 1: "))
n2=int(input("Enter the number 2: "))

print("Addition: ",calculate(n1,n2,addition))
print("Subtraction: ",calculate(n1,n2,subtraction))
print("Multiplication: ",calculate(n1,n2,multiplication))
print("division: ",calculate(n1,n2,division))
