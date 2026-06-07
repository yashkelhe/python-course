marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))

# Check for total percentage
total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed:", total_percentage)

else:
    print("You failed, try again next year:", total_percentage)



from functools import reduce

numbers = [10, 20, 30]

# x is the accumulator, y is the current element
total = reduce(lambda x, y: x + y, numbers) 




# "1. If your list contains standard items (Integers, Strings)For a simple flat list, a shallow copy feels like a deep copy because changing one list does not affect the other."
nums = [1, 2, 3]
copy_nums = nums.copy()

copy_nums[0] = 99

print(nums)       # Output: [1, 2, 3] (Original is safe)
print(copy_nums)  # Output: [99, 2, 3]

# 2. If your list contains nested items (Lists, Dictionaries)A shallow copy only copies the top-level outer structure. Any nested collections inside it still point to the exact same memory address as the original list

nums = [1, 2, [3, 4]]  # Contains a nested list
copy_nums = nums.copy()

# Modifying the inner nested list
copy_nums[2][0] = 99

print(nums)       # Output: [1, 2, [99, 4]] <--- Original changed!
print(copy_nums)  # Output: [1, 2, [99, 4]]
