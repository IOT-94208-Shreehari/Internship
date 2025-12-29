def recussion(n):
    if n==0 or n==1:
       return 1
    else:
        return n * recussion(n-1)

def power(base,exp):
    if exp == 0 :
       return 1
    else:
       return base * power (base, exp - 1)
      
num=int(input("Enter the number : "))
print(f"The factorial of number {num} is {recussion(num)}")

base = int(input("Enter the base: "))
exp = int(input("Enter the exponent: "))
print(f"The base is {base} and the exponent is {exp} the result is {power(base,exp)}")