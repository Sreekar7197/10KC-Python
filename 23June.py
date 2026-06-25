# Question 1:
# Count Valid Ages
# Use: 
# • while loop
# • continue
# • User input
# Task:
# Keep accepting ages until the user enters -1. Ignore ages below 1 and above 120. Count valid ages only. 
# Example 
# Input: 
# 25
# 150
# 40
# -5
# 18
# -1 
# Output:
# Valid ages count: 3

count = 0
while (age := int(input("Enter your age: "))) != -1:
    if age < 0 or age > 120:
        continue
    else:
        count +=1
print(f"Valid ages count: {count}")
# ****************************************************************************

# Question 2: Sum Multiples of 5
# Use:
# • while loop
# • continue
# • Modulus operator (%)
# • User input
# Task:
# Keep accepting numbers until the user enters 0.
# Add only numbers divisible by 5.
# Skip all other numbers using continue.
# Example
# Input:
# 10
# 12
# 15
# 18
# 20
# 0
# Output:
# Sum: 45

sum = 0
num = int(input("Enter a number: "))
while num!=0:
    if num %5 != 0:
        num = int(input("Enter a number: "))
        continue
    sum += num
    num = int(input("Enter a number: "))
print(f"Sum: {sum}")
# ******************************************************************************

# Question 3: Count Uppercase Letters
# Use:
# • for loop
# • continue
# • Character comparison
# Task:
# Given:
# text = "PyTHon ProGRAM"
# Count how many uppercase letters are present.
# Skip all other characters using continue.
# Expected Output:
# Uppercase letters count: 8

text = "PyTHon ProGRAM"
uppercase = 0
for letter in text:
    if "a"<= letter <="z" or letter==" ":
        continue
    uppercase+=1
print(f"Uppercase letters count: {uppercase}")
# *****************************************************************************

# Question 4: Total Sales Amount
# Use:
# • for loop
# • continue
# • if
# • Addition
# Task:
# Given:
# sales = [500, 0, 1200, 0, 700]
# Find the total sales amount.
# Entries with value 0 represent cancelled sales and should be skipped using continue.
# Expected Output:
# Total sales amount: 2400

sales = [500, 0, 1200, 0, 700]
total = 0
for sale in sales:
    if sale == 0:
        continue
    total += sale
print(f"Total sales amount: {total}")