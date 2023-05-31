cartas = input().split(' ')
cartas = list(map(int, cartas))

n = 0
boolean = False

for i in cartas:

    for j in range(n+1, len(cartas)):
        if i > j:
            boolean = True
        else:
            boolean = False

    n = n + 1

if boolean:
  print('C')