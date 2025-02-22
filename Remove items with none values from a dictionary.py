# Python program to remove items with none values from a dictionary
# Taking a dictionary as input from the user
input_dict = eval(input("Enter a dictionary with None values: "))
# Create a new dictionary excluding None values
filtered_dict = {k: v for k, v in input_dict.items() if v is not None}
print(f"Dictionary with Empty Items Dropped: {filtered_dict}")

