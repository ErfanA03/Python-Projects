#While Loops Challenge
"""
#While Loop
count = 5
while count > 0:
    print("Count:", count)
    count -= 1

    
#Break Statement
while True:
    user_input = input("Do you want to continue? (yes/no): ")
    if user_input.lower() == 'no':
        print("Exiting the loop.")
        break
    print("Still inside the loop.")

    
#Continue Statement
count = 0
while count < 5:
    count += 1
    if count == 3:
        print("Skipping count:", count)
        continue
    print("Count:", count)

    
#Else within While
count = 0
while count < 5:
    print("Count:", count)
    count += 1
else:
    print("Loop finished.")
"""

#For Loops Challenge
animals = ["dog", "cat", "monkey", "parrot", "hamster"]
nums = (1,2,3,4,5,6,7,8,9,10)

"""
#For loop
for x in animals:
    print(x)

#Break Statement
for x in animals:
    if x == "monkey":
        break
    print(x)
    
#Continue Statement
for i in nums:
    print("Count:", i)
    if i == 5:
        print("I am 5, and I got skipped :( ")
        continue

#range function within for loop
for i in range(2,10,2):
    print(i)
    
#else keyword within for loop
for i in reversed(nums):
    if i % 2 == 1:
        print("I am the number {} and I am odd!".format(i))
    else:
        print("I am the number {} and I am even!".format(i))
"""

#Loop an array challenge
"""
name = "Python"
print(len(name))

for i in enumerate(name):
    print(i)
"""
