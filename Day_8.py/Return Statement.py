print("Return Statement")

def value_added_tax(amount):
    tax = amount * 0.15
    total_amount = amount * 1.25

    return amount,tax,total_amount

print(value_added_tax(100))
price = value_added_tax(100)
print(price,type(price))
