sandwich_orders = ['sand1','sand2', 'sand3', 'pastrami', 'pastrami']
finished_sandwich = []

print('we ran out of pastrami')

i = 0

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for order in sandwich_orders:
    print(f"making {order}")
    finished_sandwich.append(order)

for order in finished_sandwich:
    print(f"made {order}")
