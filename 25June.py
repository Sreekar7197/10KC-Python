# Question 1: Student Marks Total
# Concept to Use: Nested for loop, Input, Accumulator (total)
# Problem Statement: There are 5 students and each student has marks in 3 subjects. Calculate and print the total marks of each student.
# Example Input: Student 1: 70 80 90 | Student 2: 60 75 85
# Example Output: Student 1 Total = 240 | Student 2 Total = 220

for i in range(1,6):
    print(f"Student {i}:")
    total = 0
    for j in range(1,4):
        marks = int(input())
        total += marks
    print(f"Total = {total}")
# ******************************************************************************

# Question 2: Shop Sales Report
# Concept to Use: Nested for loop, Input, Accumulator (sum)
# Problem Statement: A shop sells 4 products. For each product, enter sales for 7 days and find the total sales.
# Example Input: Product 1 -> 100 200 150 120 180 140 110
# Example Output: Product 1 Total Sales = 1000

for i in range (1,5):
    print(f"Product {i}:")
    total = 0
    for j in range(1,8):
        sales = int(input())
        total += sales
    print(f"Total Sales = {total}")
# ******************************************************************************

# Question 3: Find Highest Mark in Each Student Record
# Concept to Use: Nested for loop, Comparison, Input
# Problem Statement: There are 4 students and each student has marks in 5 subjects. Find the
# highest mark scored by each student.
# Example Input: 70 85 60 90 75
# Example Output: Highest Mark = 90

for i in range(1,5):
    print(f"Student {i}:")
    highest = 0
    for j in range(1,6):
        mark = int(input())
        if mark > highest:
            highest = mark
    print("Hightst Mark =",highest)
# ******************************************************************************

# Question 4: Theatre Seat Booking Status
# Concept to Use: Nested for loop, Conditional statements (if), Counting
# Problem Statement: A theatre has 5 rows and 6 seats in each row. Input seat status (1=Booked, 0=Empty). Count booked seats in each row.
# Example Input: 1 0 1 1 0 1
# Example Output: Row 1 Booked Seats = 4

for row in range(1,6):
    print(f"Row {row}: ")
    booked = 0
    for seat in range(1,7):
        seat = int(input())
        if seat == 1:
            booked += 1
    print(f"Booked Seats: {booked}")