# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years_left_to_90 = 90 - int(age)

# print((years_left_to_90))

months_left_to_90 = years_left_to_90 * 12

# print(months_left_to_90)

weeks_left_to_90 = years_left_to_90 * 52

# print(weeks_left_to_90)

days_left_to_90 = years_left_to_90 * 365

# print(days_left_to_90)

print(f"you have {days_left_to_90} days,{weeks_left_to_90} weeks ,{months_left_to_90} months left.")
