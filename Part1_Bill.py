print('BILL')
print()
item_count = 0
total_bill = 0
iteration_add = 1
total_receipt = {}
while iteration_add == 1:
    item_cost = float(input())
    if item_cost > 0:
        item_name = input()
        item_count = item_count + 1
        total_bill = total_bill + item_cost
        total_receipt[item_name] = item_cost
    else:
        iteration_add = 0
for i, (key, value) in enumerate(total_receipt.items()):
    print(key + ':', '{:.2f}'.format(value))
print()
print('Amount Total:', end = ' ')
print('{:.2f}'.format(total_bill))
print()
gratuity_18_total = total_bill * .18
sales_tax = total_bill * .07
print('Gratuity:', gratuity_18_total)
print('Sales tax:', sales_tax)
bill_total = total_bill + gratuity_18_total + sales_tax
print()
print('Bill total:', ('{:.2f}'.format(bill_total)))
print()
print()
print('THANK YOU FOR DINING')




