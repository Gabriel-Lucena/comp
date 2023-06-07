cartas = input().split(' ')
cartas = list(map(int, cartas))

n = 0
boolean_matrix = [False, False,False]

for i in cartas:

    for j in range(n + 1, len(cartas)):
        
        if i <= cartas[j]:
            boolean_matrix[0] = True
        else:
            boolean_matrix[0] = False
            break

    if boolean_matrix[0] == False:
        break

    n = n + 1

if boolean_matrix[0] == False:
    
    for i in cartas:
        
        for j in range(n + 1, len(cartas)):
            
            if i >= cartas[j]:
                
                boolean_matrix[1] = True
            else:
                boolean_matrix[1] = False
                
                break
    
        if boolean_matrix[1] == False:
            break
    
        n = n + 1
    

if boolean_matrix[0]:
    print('C')
elif boolean_matrix[1]:
    print('D')
else:
    print('N')