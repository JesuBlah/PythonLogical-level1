divisor = int(input("Enter the divisor: "))
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
divisible_numbers = []

for num in range(start, end + 1):
    if num % divisor == 0:
        divisible_numbers.append(num)

print("Numbers divisible by", divisor, "between", start, "and", end, "are:", divisible_numbers)
