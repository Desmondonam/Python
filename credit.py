price = 1000000

good_credit = False

if good_credit:
    down_payment = price * 0.1
    print(down_payment)
else:
    down_payment = price * 0.2
    print(down_payment)




 # the improved Version of it is as follows

if good_credit:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2
print(f"Down payment: ${down_payment}")
