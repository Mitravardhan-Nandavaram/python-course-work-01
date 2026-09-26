data = {
    'darkchocolate':5.99,
    'soap':10.00,
    'toothpaste':20.00,
    'eggs':49.99,
    'rice':200.00,
    'butter':150.00,
    'biscuits':25.00,
    'oil':30.00,
    'salt':20.00
}

for i in data:
    print(i.ljust(20), data[i])
    product = input("Enter the products: ").split()
    print("----------Bill---------------")
    bill = 0
    while True:
        product = input("Enter the product name or [E]xit:")
        if product == 'E' or product == 'e':
            print("Thanks for shopping")
            print("Total bill:",bill)
            break
        else:
            quantity = int(input("Enter the quantity:"))
            bill += data[product]*quantity

    