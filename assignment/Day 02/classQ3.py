def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci series:")
    for i in range(n):
        print(a, end=" ")
        temp = a + b
        a = b
        b = temp

terms = int(input("Enter the number of terms: "))
fibonacci(terms)
