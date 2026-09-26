buget = int(input("Enter the budget:"))
if budget > 10000:
    print("Trip")
elif budget > 5000:
    print("Resort Stay")
elif budget > 3000:
    print("Movie an Dinner")
elif budget > 1000:
    print("Cafe and Shopping")
elif budget > 500:
    print("Street Food and Park Visit")
else:
    print("Stay Home")
        