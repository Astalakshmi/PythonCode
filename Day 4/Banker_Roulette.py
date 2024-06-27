import random

names = ["asta", "palani", "navisha", "dheekshaa"]
# Get the total number of items in list.
length = len(names)
# Generate random numbers between 0 and the last index.
random_names1 = random.randint(0,length-1)
print(random_names1)
# Choose and print a random name.
print(names[random_names1])


