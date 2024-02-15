start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))
armstrong_numbers = []

for num in range(start, end + 1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if num == sum:
        armstrong_numbers.append(num)

print("Armstrong numbers between", start, "and", end, "are:", armstrong_numbers)