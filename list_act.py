# 1. Basic List Activities

# Activity 1: Create a List
fruits = ["apple", "banana", "cherry"]
print("Activity 1:", fruits)

# Activity 2: Access Items
fruits = ["apple", "banana", "cherry"]
print("Activity 2 - First item:", fruits[0])
print("Activity 2 - Last item:", fruits[-1])

# Activity 3: List Length
colors = ["red", "blue", "green", "yellow"]
print("Activity 3 - Length of colors list:", len(colors))

# 2. Modify Lists

# Activity 4: Change Item
fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"
print("Activity 4:", fruits)

# Activity 5: Add Items
fruits = ["apple", "banana"]
fruits.append("mango")     
fruits.insert(1, "grape")    
print("Activity 5:", fruits)

# Activity 6: Remove Items
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")  
fruits.pop()             
print("Activity 6:", fruits)

# 3. Looping Through Lists

# Activity 7: For Loop
animals = ["dog,", "cat,", "bird"]
print("Activity 7:", end=" ")
for animal in animals:
    print(animal, end=" ")
print()

# Activity 8: With Index
numbers = [10, 20, 30]
print("Activity 8:")
for index, value in enumerate(numbers):
    print(index, ":", value)


# 4. List Operations

# Activity 9: Check if Item Exists
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Activity 9: Banana is in the list")

# Activity 10: Sorting
numbers = [5, 2, 9, 1]
numbers.sort()             
print("Activity 10 - Ascending:", numbers)
numbers.sort(reverse=True) 
print("Activity 10 - Descending:", numbers)

# Activity 11: Copy List
list1 = ["a", "b", "c"]
list2 = list1.copy()
print("Activity 11:", list2)
