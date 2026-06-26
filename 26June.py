# Problem 1 – Nested while
# What is the problem asking?
# Generate all pairs from 1–5 and print only pairs whose sum is even.
# Things needed for logic:
# • Outer while → first number (i)
# • Inner while → second number (j)
# • Addition: i+j
# • Condition: (i+j)%2==0
# Example dry run:
# i=1, j=1 → sum=2 → print
# i=1, j=2 → sum=3 → skip
# Example output:
# (1,1)
# (1,3)
# (1,5)
# (2,2)...

i=1
while i<=5:
    j=1
    while j<=5:
        if (i+j)%2 == 0:
            print(f"({i},{j})")
        j+=1
    i+=1
# ******************************************************************************

# Problem 2 – Nested while
# What is the problem asking?
# Generate all pairs from 1–10 and print only pairs whose product is greater than 30. Also count total
# pairs.
# Things needed for logic:
# • Outer while
# • Inner while
# • Multiplication: i*j
# • Condition: i*j > 30
# • Counter variable
# Example output:
# (4,8) → 32
# (4,9) → 36

i = 1
while i<=10:
    j=1
    while j<=10:
        if i*j > 30:
            print(f"({i},{j}) -> {i*j}")
        j +=1
    i+=1
# ******************************************************************************

# Problem 3 – For inside While
# What is the problem asking?
# Keep asking user for numbers until 0 is entered. For each number, find factors and their sum.
# Things needed for logic:
# • while num!=0
# • for i in range(1,num+1)
# • Factor condition: num%i==0
# • Sum variable
# Example:
# Input:12
# Factors:1 2 3 4 6 12
# Sum:28

num = int(input("Input:"))
while num!=0:
    sum=0
    print("Factors:",end="")
    for i in range(1,num+1):
        if num%i==0:
            print(i,end=" ")
            sum += i
    print()
    print(f"Sum:{sum}")    
    num = int(input("Enter a number: "))

# ******************************************************************************

# Problem 4 – While inside For
# What is the problem asking?
# Given numbers=[12,7,20,9], for each number print values from 1 to that number and count evens.
# Things needed for logic:
# • for through list
# • while loop for counting
# • Even condition: i%2==0
# • Counter variable
# Example output:
# 12 → Even count: 6
# 7 → Even count: 3

numbers=[12,7,20,9]
for num in numbers:
    even = 0
    i=1
    while i<= num:
        if i % 2 == 0:
            even += 1
        i+=1
    print(f"{num} -> Even count: {even}")