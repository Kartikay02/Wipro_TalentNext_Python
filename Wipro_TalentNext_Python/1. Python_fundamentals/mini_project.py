# MINI PROJECTS

# 1. Travel Suggestion

# Ask the user how far they want to travel
distance = float(input("How far would you like to travel in miles? "))

# Determine the travel suggestion based on the distance
if distance < 3:
    print("I suggest Bicycle to your destination")
elif 3 <= distance < 300:
    print("I suggest Motor-cycle to your destination")
else:
    print("I suggest Super-Car to your destination")


# 2. Cloud Server Cost Calculator

# Hosting provider charges per hour
cost_per_hour = 0.51

# Calculate costs
cost_per_day = cost_per_hour * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30

# Calculate how many days you can operate with $918
total_budget = 918
days_operable = total_budget / cost_per_day

# Display the results
print(f"Cost to operate one server per day: ${cost_per_day:.2f}")
print(f"Cost to operate one server per week: ${cost_per_week:.2f}")
print(f"Cost to operate one server per month: ${cost_per_month:.2f}")
print(f"Days you can operate one server with ${total_budget}: {int(days_operable)} days")
