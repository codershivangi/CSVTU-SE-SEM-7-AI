def calculate_average(numbers):

    if not numbers:
        raise ValueError("List cannot be empty")

    total = sum(numbers)
    average = total / len(numbers)

    return average


# Main program
marks = [80, 75, 90, 85]

result = calculate_average(marks)

print("Marks:", marks)
print("Average Marks:", result)