a = [2,1,2,3,4,5]
# Append adds items to the back of the list
a.append(6)
# Insert inserts an item at a specific position
a.insert(0, 0)
print(a)

# Removing elements
a.remove(3)
# Pop an element at a specific position, defaults to the end
print(a.pop())
print(a.pop(1)) # Popped the 2nd element
print(a)

words = ["Tower", "Hat", "Chair"]
b = ["Tower", "Cat"]
# copy function
words2 = words.copy()
# extends function
words.extend(b)
# count function
print(words.count("Tower"))
print(words)

#       0,1,2,3,4,5,6,7,8,9
nums = [1,2,3,4,5,6,7,8,9,10]
# Using indices (plural of index)
print(nums[4]) # Getting the 5th index of the list
# # Get the last element of the list
print(nums[-1])

# # Slicing
print(nums[:5]) #exclusive
print(nums[5:]) #inclusive
print(nums[1:9]) #prints all elements from 2 to 9
print(nums[1:10:2]) # prints all even elements in the list

# 2D List / Matrix
list2D = [[1,2,3], 
		  [4,5,6], 
		  [7,8,9]]
# the number 6 is in the 2nd list (position 1), at the 3rd index (position 2)
print(list2D[1][2])

for i in range(3):
	for j in range(3):
		print(list2D[i][j])

# Tuples are defined with round brackets()
myths = ("Zeus", "Hera", "Heracles")
# Tuples cannot be changed
# myths[2] = "Hercules"
