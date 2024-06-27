print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L:")  # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni? Y or N:")  # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese? Y or N:")  # Do you want extra cheese? Y or N
add_pepper = 0
ex_cheese = 0
if size == "S":
    small_size = 15
    if add_pepperoni == "Y":
        add_pepper = small_size + 2

    elif add_pepperoni == "N":
        add_pepper = small_size + 0

    if extra_cheese == "Y":
        ex_cheese = add_pepper + 1

    elif extra_cheese == "N":
        ex_cheese = add_pepper + 0
    print(f"Your final bill is: ${ex_cheese}.")
if size == "M":
    medium_size = 20
    if add_pepperoni == "Y":
        add_pepper = medium_size + 3

    elif add_pepperoni == "N":
        add_pepper = medium_size + 0

    if extra_cheese == "Y":
        ex_cheese = add_pepper + 1

    elif extra_cheese == "N":
        ex_cheese = add_pepper + 0
    print(f"Your final bill is: ${ex_cheese}.")

if size == "L":
    large_size = 25
    if add_pepperoni == "Y":
        add_pepper = large_size + 3

    elif add_pepperoni == "N":
        add_pepper = large_size + 0

    if extra_cheese == "Y":
        ex_cheese = add_pepper + 1

    elif extra_cheese == "N":
        ex_cheese = add_pepper + 0
    print(f"Your final bill is: ${ex_cheese}.")
