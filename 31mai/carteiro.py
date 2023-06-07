quantities = input().split(' ')

order_houses = input().split(' ')

order_deliveries = input().split(' ')

def find_index(vector, value):

  n = 0

  for i in vector:
    
    if i == value:
      return n
    
    n += 1

n = 0

steps  = 0

for delivery in order_deliveries:
  
  if n == 0:  
    steps += find_index(order_houses, delivery)
  else:
    steps += abs(find_index(order_houses, delivery) - find_index(order_houses, order_deliveries[n - 1]))
  
  
  n += 1

print(steps)