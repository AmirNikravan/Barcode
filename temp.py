# Starting number
number = 1

# Function to format number with leading zeros
def format_number(n, width=7):
    return f"{n:0{width}}"

# Increment the number and format it
for i in range(10):
    formatted_number = format_number(number)
    print(formatted_number)
    number += 1
