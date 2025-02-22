#Concatenate Multiple Dictionaries
# Define three sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Create an empty dictionary to store the result
merged_dict = {}

# Merge the first dictionary into merged_dict
merged_dict.update(dic1)

# Merge the second dictionary into merged_dict
merged_dict.update(dic2)

# Merge the third dictionary into merged_dict
merged_dict.update(dic3)

# Print the final merged dictionary
print("Merged Dictionary:", merged_dict)
