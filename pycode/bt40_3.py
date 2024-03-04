
# Power Calculation:

def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

# Example usage
print(power(2, 3))  # Output: 8