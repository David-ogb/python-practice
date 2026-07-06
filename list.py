# largest number
# nums = []
# for x in range(3):
    # num = int(input("Enter a number: "))
    # nums.append(num)
# print(f"{max(nums)} is the largest")




#program to get 5 nubers and print the max, min and number of even and odd
#empty list container to add the numbers
# numbers = []
#add them 5 times
# for x in range(5):
    # num = int(input("Enter a number: "))
    # numbers. append(num)
#check them
# print (numbers)
#print largest and smalles
# print(f"Largest: {max(numbers)}")
# print(f"Smallest: {min(numbers)}")
#containers to increase as even and odd increase
# even = 0
# odd = 0
#run through them and check for even and odd
# for num in numbers:
#     if num % 2 == 0:
#         even += 1
#     else:
#         odd += 1

# print(f"Even numbers: {even}")
# print(f"Odd numbers: {odd}")


#program to remove duplicates and cout them

# #to create and print the list
# numbers = []
# for x in range(7):
#     num = int(input("Enter a number: "))
#     numbers.append(num)

# print(f"Original: {numbers}")

# unique = []
# duplicates = 0 
#check if the number is in the list
# for num in numbers: 
#     if num not in unique:
#         unique.append(num)
#     else:
#         duplicates += 1

# print(f"Unique {unique}")
# print(f"Duplicates removed: {duplicates}")
    

word = input("Enter a word: ").lower()
vowel = 0
consonant = 0

for letter in (word):
    if ("a" in letter) or ("e" in letter) or ("i" in letter) or ("o" in letter) or ("u" in letter):
        vowel += 1
    else:
        consonant += 1

print(f"Vowels: {vowel}")
print(f"Consonants: {consonant}")