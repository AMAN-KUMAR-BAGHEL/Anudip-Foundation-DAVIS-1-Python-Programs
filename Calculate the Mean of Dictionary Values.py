#Calculate the Mean of Dictionary Values
# Define the dictionary with key-value pairs
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}

# Calculate the sum of all values in the dictionary
total = sum(test_dict.values())

# Count the number of elements in the dictionary
count = len(test_dict)

# Compute the mean (average) by dividing the total sum by the count
mean = total / count

# Print the calculated mean
print("Mean:", mean)
