programming_dictionary={"Loop":"An action of repeating something again and again","Python":"Python is Fun"}
print(programming_dictionary["Loop"])

# Adding data to dictionary
programming_dictionary["Bug"]="Error in program"

print(programming_dictionary)

# Wipe an existing dictionary
programming_dictionary={}
print(programming_dictionary)

# Edit data to dictionary
programming_dictionary["Bug"]="A moth in your computer"
print(programming_dictionary)

# loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])