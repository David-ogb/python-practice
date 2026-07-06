#program  to print a pyramid

blocks = int(input("Enter the number of blocks: "))

total = 0
height = 0
max_height = 0

#condition to start counting
while total < blocks:
    #increasing the height based on the total
    height += 1
    total += height
    #to ensure that the the height does not exceed the block
    if total <= blocks:
        max_height = height

print(f"The height of the pyramid is {max_height}")
        
