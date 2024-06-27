score = int(input("Enter the Score:"))
if score >= 90:  # score is above 90
    print("Grade A")
elif score >= 80:  # score is between 80 and 90
    if score >= 85:  # score is greater 85
        print("Grade A-")
    else:
        print("Grade B+")
elif score < 80:  # score is smaller 80
    if score >= 70:  # score is  greater 70
        print("Grade C")
    else:
        print("Grade D")

