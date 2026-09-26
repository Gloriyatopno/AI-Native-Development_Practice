#wrong code
def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average


print(calculate_average([]))

#GitHub Copilot suggested code:
def calculate_average(numbers):
    if not numbers:
        return 0

    total = sum(numbers)
    return total / len(numbers)


print(calculate_average([]))        # 0
print(calculate_average([2, 4, 6])) # 4.0