#1  Build a subject report from a student list
# You are given a list of student records, where each record is a dictionary containing a student's name
# and their score in three subjects. Loop through each student and print a one-line summary showing
# their name, total score, and whether they passed overall. A student passes overall if their total score
# is 150 or more out of 300.
from unittest import result

students = [
  {"name": "Ali",  "math": 72, "english": 65, "science": 80},
  {"name": "Mia",  "math": 40, "english": 55, "science": 45},
  {"name": "Joe",  "math": 90, "english": 88, "science": 76},
  {"name": "Sara", "math": 30, "english": 42, "science": 38}
]
for student in students:
    total = sum([student["math"] + student["english"] + student["science"]])
    result = "PASS" if total >= 150 else "FAIL"
    print(student["name"], "| Total:", total, "|", result)


#2 Categorize a shopping cart by price range
# You are given a list of items, where each item is a dictionary with a name and a price. Loop through
# the list and sort items into three separate lists: 'cheap' (under $20), 'mid' (between $20 and $99
# inclusive), and 'expensive' ($100 or more). At the end, print each category and the names of items in
# it.
cart = [
  {"name": "Pen", "price": 3},
  {"name": "Headphones", "price": 120},
  {"name": "Notebook", "price": 15},
  {"name": "Keyboard", "price": 75},
  {"name": "Monitor", "price": 350},
  {"name": "Cable", "price": 8},
  {"name": "Mouse", "price": 45 }
]
cheap = []
mid = []
expensive = []
for item in cart:
    if item["price"] < 20:
        cheap.append(item["name"])
    elif item["price"] <= 99:
        mid.append(item["name"])
    else:
        expensive.append(item["name"])
print("Cheap:", cheap)
print("Mid:", mid)
print("Expensive:", expensive)


#3  Find the top scorer per subject across all students
# Given a list of student dictionaries, each containing a name and scores for multiple subjects, write
# code that finds the name of the student who scored highest in each subject. Build a result dictionary
# where each subject maps to the top scorer's name. If two students tie on a subject, keep the one who
# appears first in the list.
#Method 1
students = [
  {"name": "Ali", "math": 88, "science": 72, "english": 90},
  {"name": "Mia", "math": 95, "science": 88, "english": 76},
  {"name": "Joe", "math": 70, "science": 95, "english": 90},
  {"name": "Eva", "math": 95, "science": 60, "english": 85}
]
subjects = ["math", "science", "english"]
result = {}
for subject in subjects:
    highest_student = students[0]
    for student in students:
        if student[subject] > highest_student[subject]:
            highest_student = student
    result[subject] = highest_student["name"]
print(result)

#Method 2
students = [
  {"name": "Ali", "math": 88, "science": 72, "english": 90},
  {"name": "Mia", "math": 95, "science": 88, "english": 76},
  {"name": "Joe", "math": 70, "science": 95, "english": 90},
  {"name": "Eva", "math": 95, "science": 60, "english": 85}
]
result = {subject: max(students, key=lambda x: x[subject])["name"]
          for subject in ["math", "science", "english"]}
print(result)


#4  Build an inventory summary with low-stock alerts
# You are given an inventory as a dictionary where each key is a product name and the value is another
# dictionary with 'stock' and 'price'. Loop through the inventory and print a summary line for each
# product. If stock is 10 or below, add a LOW STOCK warning. At the end, print the total inventory value
# (sum of stock x price for all products) and a list of all low-stock product names.
inventory = {
  "Apple":  {"stock": 120, "price": 0.5},
  "Banana": {"stock": 8,   "price": 0.3},
  "Mango":  {"stock": 35,  "price": 1.2},
  "Cherry": {"stock": 5,   "price": 2.0},
  "Grape":  {"stock": 60,  "price": 0.8}
}
total_value = 0
low_stock = []
for product, details in inventory.items():
    stock = details["stock"]
    price = details["price"]
    value = stock * price
    total_value += value
    print(product, "| Stock:", stock, "| Value:", value)
    if stock < 10:
        print("⚠️ LOW STOCK")
        low_stock.append(product)
print("Total inventory value:", total_value)
print("Low stock items:", low_stock)