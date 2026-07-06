# print('Grep\'s book')
# print("'Greg\'s book.")
# print(0o76353) #octaldecimval 0o
# print(0x329AE) #Hexadecimal 0x
# #quote in a string
# print("I\'m David")
# print("I'm David")
# print("\"I'm\" \n \"\"learning\"\" \n \"\"\"Python\"\"\"")    
#print(1 // 2 * 3)

#dictionaries

capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Mascow"}

# get a value from a key
#print(capitals.get("Japan"))

#add to dictionary
#capitals.update({"Germany": "Berlin"})
#print(capitals.get("Germany"))

#update dict
#capitals.update({"USA": "Detroit"})
#print(capitals.get("USA"))

#remove key:value pair
#capitals.pop("China")
#print(capitals)

#remove last item
#capitals.popitem()

#to get keys only
#keys = capitals.keys()
#print(keys)

#for key in keys:
#    print(key)

# values = capitals.values()
# for value in values:
#     print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")

fruits = ['apples', 'orange', 'banana', 'eggs']
print(fruits[3])