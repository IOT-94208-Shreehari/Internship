num=int(input("Enter the five digit number: "))
print("The Entered number is",num)
temp = num
rev=0

while num > 0 :
    digit = num % 10
    rev=rev * 10 + digit
    num= num // 10

if rev == temp:
    print(f"The Entered number",temp,"is paliendrome number")
else:
    print("Entered number is not a palindrome number")
 