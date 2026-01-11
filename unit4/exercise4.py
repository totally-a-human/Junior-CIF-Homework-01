def numbers(list):
    list = list.split(",")
    list = [int(i) for i in list]
    list_sum = sum(list)
    print(f"The sum of the numbers {list} is {list_sum}.")
    return "summed"

results = numbers(list=input("Enter a list of numbers, separated by commas: "))
print(results)