# Stephanie Ramos
# March 23, 2025
# Module 1.3 Assignment

# Calculate the cost of installing fiber optic cable
def calculate_fiber_cost(feet):
    price_per_foot = 0.87
    total_cost = feet * price_per_foot
    return total_cost, price_per_foot

# Welcome message
print ('Welcome to Total Fiber!')

# Get the amount in feet to be installed
feet = 100.0  # Example value, can be replaced with input

# Call the function to calculate cost
total_cost, price_per_foot = calculate_fiber_cost(feet) 

# Calculated cost and company name.
print(f"Feet to be installed: {feet}")
print(f"Rate per foot: ${price_per_foot:.2f}")
print(f"Installation total: ${total_cost:.2f}")
print("Company: Total Fiber")