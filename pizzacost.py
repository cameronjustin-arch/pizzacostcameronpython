import math

# Start of the program
print("Lets calculate the total of the pizza!")

# Ask user for inputs
# We use float() because diameters and tax rates usually have decimals
diameter = float(input("What is the diameter? (Inches): "))
tax_rate = float(input("What is the tax? (example=0.13): "))

# Calculate subtotal based on your formula: 0.75 + 1 + (0.5 * diameter)
subtotal = 0.75 + 1 + (0.5 * diameter)
print(f"The subtotal is ${subtotal:.2f}")

# Calculate the tax amount
real_tax = subtotal * tax_rate

# Your blocks show a manual rounding process: 
# (multiply by 100, round, then divide by 100)
real_tax = round(real_tax * 100) / 100
print(f"The tax is ${real_tax:.2f}")

# Calculate the final total
total = subtotal + real_tax

# Apply the same rounding logic to the total
total = round(total * 100) / 100
print(f"The total is ${total:.2f}")