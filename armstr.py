#program to determine an armstrong number

num = int(input("Enter a number: "))
#convert the number to string
num = str(num)
#counts the numbers in it, then save the value
count = len(num)

#convert back to an integer
num = int(num)

nums = []
nums.append(num)
for x in nums:
    print(x)
print(type(nums))