area_telescopio = int(input())

quantidade_estrelas = int(input())

estrelas = []

quantidade_estrelas_visiveis = 0

for i in range(quantidade_estrelas):
    estrelas.append(int(input()))
    if estrelas[i] * area_telescopio >= 40000000:
        quantidade_estrelas_visiveis += 1


print(quantidade_estrelas_visiveis)
