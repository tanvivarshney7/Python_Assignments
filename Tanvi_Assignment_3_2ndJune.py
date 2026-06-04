#1. Print all items in a list
#Given a list of fruits, use a for loop to print each fruit on a new line.
fruits = ["apple", "banana", "cherry", "mango"]
for fruit in fruits:
    print(fruit)


#2. Sum all numbers in a list
#Given a list of numbers, use a for loop to calculate and print their total sum. Do not use the built-in
# sum() function.
nums = [4, 7, 2, 9, 1, 5]
total = 0
for i in nums:
    total += i
print(total)


#3. Count even numbers in a list
#Given a list of integers, use a for loop and an if statement to count how many numbers are even.
nums = [1, 2, 3, 4, 5, 6, 7, 8]
count = 0
for i in nums:
    if i % 2 == 0:
        count += 1
print(count)


#4. Print all keys and values from a dictionary
#Given a student dictionary, use a for loop to print each key and its value on one line.
student = {"name": "Tanvi", "age": 29, "grade": "A", "city": "Toronto"}
for key,value in student.items():
    print(key, ":", value)


#5. Find the largest number in a list
#Without using max(), loop through a list and track the largest number seen so far.
nums = [3,16,9,14,27,25]
largest = nums[0]
for num in nums:
    if num > largest:
        largest = num
print(largest)


#6. Skip a specific item using continue
#Loop through a list of names and print each one — but skip the name 'Bob' using continue.
names = ["Alice", "Bob", "Charlie", "Diana", "Bob", "Eve"]
for name in names:
    if name == "Bob":
        continue
    print(name)


#7. Stop a loop early using break
#Loop through a list of numbers and print each one. As soon as you encounter the number 0, stop the loop
# using break. Do not print 0.
nums = [1,4,2,0,2,7,6,8,9]
for num in nums:
    if num == 0:
        break
    print(num)


#8. Separate odd and even numbers into two lists
#Given a list of integers, use a for loop and if/else to build two separate lists — one for even numbers and
# one for odd numbers.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
odds = []
for num in nums:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)
print("Evens:", evens)
print("Odds:", odds)


#9. Count how many students passed
#Given a dictionary of student names and scores, loop through it and count how many students scored 50 or
# above (passing mark).
scores = {
    "Ali":72,
    "Mia":45,
    "Joe":88,
    "Sam":39,
    "Eva":60,
    "Leo":50
}
count = 0
for key, value in scores.items():
    if value >= 50:
        count += 1
print(count, "students passed")


#10. Reverse a list using a loop
#Without using .reverse() or slicing, use a for loop to build a new reversed version of the list.
#Method 1
lst = [1,2,3,4,5]
reverse_list = []
for i in range(len(lst)-1, -1, -1):
    reverse_list.append(lst[i])
print(reverse_list)

#Method 2
lst = [1,2,3,4,5]
reverse_list = []
for i in lst:
    reverse_list.insert(0, i)
print(reverse_list)


#11. Print a multiplication table
#Given a number n, use a for loop to print its multiplication table from 1 to 10.
n = 7
for i in range(1, 11):
    print(n, "x", i, "=", n * i)


#12. Find the student with the highest score
#Given a dictionary of student names and scores, loop through it to find and print the name of the student
# with the highest score.
#Method 1
scores = {
    "Ali":72,
    "Mia":95,
    "Joe":88,
    "Sam":61,
    "Eva":90
}
top_student = ""
highest = 0
for student in scores:
    if scores[student] > highest:
        highest = scores[student]
        top_student = student
print(top_student)

#Method 2
scores = {
    "Ali":72,
    "Mia":95,
    "Joe":88,
    "Sam":61,
    "Eva":90
}
top_student = ""
highest = 0
for key, value in scores.items():
    if value > highest:
        highest = value
        top_student = key
print(top_student)


#13. Remove all negative numbers from a list
#Given a list of integers, use a for loop and an if statement to build a new list containing only
# non-negative numbers.
nums = [3, -1, 4, -7, 5, -2, 8, 0]
result = []
for i in nums:
    if i >= 0:
        result.append(i)
print(result)


#14. Find the first repeated item in a list
#Loop through a list and track seen items. Use break to stop as soon as you find the first item that has
# appeared before.
items = ["apple", "banana", "cherry", "banana", "mango", "apple"]
seen = []
for item in items:
    if item in seen:
        print("First repeated item:", item)
        break
    seen.append(item)


#15. Squares of even numbers using list comprehension
#Use a single list comprehension to produce a list of squares of all even numbers from 1 to 20.
square = [i*i for i in range(1,21) if i % 2 == 0]
print(square)


#16. Filter long words using list comprehension
#Given a list of words, use a list comprehension to keep only words that are longer than 4 characters.
words = ["cat","elephant","dog","python","ox","tiger","ant","crocodile"]
new_list = [word for word in words if len(word) > 4]
print(new_list)


#17. Invert a dictionary using a for loop
#Given a dictionary, loop through it and build a new dictionary where keys and values are swapped.
#Method 1 (dictionary comprehension)
codes = {"IN": "India", "US": "USA", "CA": "Canada", "UK": "Britain"}
swapped = {value: key for key, value in codes.items()}
print(swapped)

#Method 2
codes = {"IN": "India", "US": "USA", "CA": "Canada", "UK": "Britain"}
swapped = {}
for key, value in codes.items():
    swapped[value] = key
print(swapped)


#18. Group numbers into positive, negative, and zero
#Given a list of numbers, loop through and sort them into three separate lists using if/elif/else.
nums = [4, -2, 0, 7, -5, 0, 3, -1, 8]
positive = []
negative = []
zero = []
for num in nums:
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)
    else:
        zero.append(num)
print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)


#19. Build a dict comprehension of word lengths
#Given a list of words, use a dict comprehension to create a dictionary where each word is the key and
# its length is the value.
words = ["python", "loop", "dict", "comprehension", "list"]
new_dict = {word: len(word) for word in words}
print(new_dict)


#20. FizzBuzz
#Loop through numbers 1 to 30. Print 'Fizz' for multiples of 3, 'Buzz' for multiples of 5, 'FizzBuzz' for
# multiples of both, and the number otherwise.
#Method 1 (print numbers on next line)
for i in range(1,31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#Method 2 (print numbers on same line)
for i in range(1,31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end = " ")
    elif i % 3 == 0:
        print("Fizz", end = " ")
    elif i % 5 == 0:
        print("Buzz", end = " ")
    else:
        print(i, end = " ")
print()   # this print is used to move the cursor to the next line.


#21.  Find all common elements between two lists
#Given two lists, use a for loop and an if statement to find all elements that appear in both lists. Store
# results in a new list.
#Method 1
a = [1, 2, 3, 4, 5, 6]
b = [4, 5, 6, 7, 8, 9]
common = []
for num in a:
    if num in b:
        common.append(num)
print(common)

#Method 2 (List Comprehension)
a = [1, 2, 3, 4, 5, 6]
b = [4, 5, 6, 7, 8, 9]
common = [num for num in a if num in b]
print(common)

#22. Count word frequency in a sentence
#Given a sentence, split it into words and use a for loop with if/else to build a dictionary that counts how
# many times each word appears.
sentence = "the cat sat on the mat the cat"
words = sentence.split()
freq = {}
for word in words:
    if word not in freq:
        freq[word] = 1
    else:
        freq[word] += 1
print(freq)


#23. Skip multiples of 3 and stop at 50
#Loop through numbers 1 to 100. Use continue to skip any multiple of 3, and use break to stop once you
# exceed 50. Print every number that passes through.
for i in range(1, 101):
    if i % 3 == 0:
        continue
    elif i > 50:
        break
    else:
        print(i, end = " ")
print()


#24. Flatten a nested list using list comprehension
#Given a list of lists, use a list comprehension with two for clauses to flatten it into a single list.
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flatten = [item for sublist in nested for item in sublist]
print(flatten)


#25. Build a frequency dictionary and find the most common item
#Given a list of items, use a for loop to build a frequency dictionary. Then loop through the dictionary to
# find the item that appears the most.
#Method 1
items = ["apple","banana","apple","cherry","banana","apple","mango","banana"]
freq = {}
for item in items:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1
for key, value in freq.items():
    print(key, ":", value)
highest = 0
most_common = ""
for key, value in freq.items():
    if value > highest:
        highest = value
        most_common = key
print("Most common:", most_common)


#26. Dict comprehension — pass or fail per student
#Given a dictionary of student scores, use a dict comprehension to create a new dictionary where each
# student maps to 'Pass' if score >= 50, otherwise 'Fail'.
scores = {"Ali":72, "Mia":45, "Joe":88, "Sam":39, "Eva":60}
result = {name: "Pass" if marks >= 50 else "Fail"
          for name, marks in scores.items()}
print(result)


#27. Find the second largest number without sorting
#Loop through a list using if/elif to track both the largest and second largest number as you go. Do not
# sort the list.
nums = [-2,-4,4,-2,-1,-7,-2]
largest = float('-inf')
second_largest = float('-inf')
for num in nums:
    if num > largest:
        second_largest = largest
        largest = num
    elif largest > num > second_largest:
        second_largest = num
print("Second largest:", second_largest)


#28. Group words by their first letter
#Given a list of words, use a for loop and if/else to build a dictionary where each key is a letter and the
# value is a list of words starting with that letter.
words = ["apple","avocado","banana","blueberry","cherry","apricot","cantaloupe"]
result = {}
for word in words:
    first_letter = word[0]
    if first_letter in result:
        result[first_letter].append(word)
    else:
        result[first_letter] = [word]
print(result)


#29. List comprehension with nested condition
#Use a list comprehension to go through numbers 1 to 50 and keep only those that are divisible by 2
# but NOT divisible by 6.
result = [num for num in range(1,51) if num % 2 == 0 and num % 6 != 0]
print(result)


#30. Rotate a list by n positions using a loop
#Given a list and a number n, use a for loop to move the first n items to the end of the list one at a time
# using list operations. Do not use slicing.
lst = [1, 2, 3, 4, 5, 6, 7]
n = 3
for i in range(n):
    first = lst.pop(0)
    lst.append(first)
print(lst)

