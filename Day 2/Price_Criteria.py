print("*****Pricing Criteria*****")
age = int(input("Enter the Age:"))
if age <= 12:
    print("*****For children Price List********")
    Days = input("weekends or weekdays ?:")
    if Days == "weekends":
        print("The Price is $10")
    elif Days == "weekdays":
        print("The Price is $7")
elif age >= 13:
    if age <= 19:
        print("*****For Teenagers Price List********")
        Days = input("weekends or weekdays ?:")
        if Days == "weekends":
            print("The Price is $12")
        elif Days == "weekdays":
            print("The Price is $8")
    if age >= 20:
        print("*****For Adult Price List********")
        Days = input("weekends or weekdays ?:")
        if Days == "weekends":
            print("The Price is $15")
        elif Days == "weekdays":
            print("The Price is $10")
