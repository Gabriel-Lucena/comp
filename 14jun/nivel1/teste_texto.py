import sys

sys.stdin = open('teste_texto.txt', 'r')

tamanho = list(map(int, input().split()))

print(tamanho)