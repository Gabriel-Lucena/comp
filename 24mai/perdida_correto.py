qtde_pecas = int(input())
pecas = input().split('')
pecas = list(map(int, pecas))

for peca in range(1, qtde_pecas+1):
  if peca not in pecas:
    print(peca)
    break