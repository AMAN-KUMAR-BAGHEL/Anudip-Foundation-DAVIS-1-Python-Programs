# Python program to print keys, values, and items of a dictionary
# Taking a dictionary as input from the user
dict_num = eval(input("Enter a dictionary: "))
# Print keys and values
print("key\tvalue")
for key, value in dict_num.items():
    print(f"{key}\t{value}")
print()
