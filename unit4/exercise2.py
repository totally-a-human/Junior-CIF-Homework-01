def divisable(num1, num2):
    if num1 % num2 == 0:
        print(f"{num1} is divisible by {num2}.")
        return True
    else:
        print(f"{num1} is not divisible by {num2}.")
        return False
    
results = divisable(int(input("Enter first number: ")), int(input("Enter second number: ")))
print(results)