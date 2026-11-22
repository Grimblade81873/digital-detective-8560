# Number Converter
# Converts a decimal number to binary and hexadecimal

decimal_input = input("Enter a positive decimal number: ")
number = int(decimal_input)

binary_result = bin(number)
hexadecimal_result = hex(number)

print(f"Decimal: {number}")
print(f"Binary: {binary_result}")
print(f"Hexadecimal: {hexadecimal_result}")
