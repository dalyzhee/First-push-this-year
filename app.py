# This is a python program that reads data from a file, process it and sort the data and create a tuple
# the finally save it in output file.

# Step 1: Read data from input file
input_data = []

with open("input.txt", 'r') as file:
    input_data = file.readlines()
title = input_data[0]
input_data = input_data[1:]
data = []
print("Unprocessed Data from input file.")
for line in input_data:
    line = line.strip( )
    if line:
        name, age, score = line.split(',')
            # print(name.strip( ), age.strip( ), score.strip( ))
        person_data = (str(name.strip()), str(age.strip()), str(score.strip()))
        
        print(person_data)
        data.append(person_data)
# Sort the list by age in ascending order
sorted_data = sorted(data, key=lambda x: x[1])
# Print the sorted list
print()
print("Processed Data.")
with open("output.txt", 'w') as output:
        output.write(title)
        for item in sorted_data:
            
            print(item)
            item_str = ', '.join(item)  # Convert the tuple to a comma-separated string
            output.write(item_str + '\n')

    
# # print(title)