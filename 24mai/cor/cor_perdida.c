#include <stdio.h>
int main()
{
  int qtde, i, pecas[1000];

  scanf("%d", &pecas);

  for (i = 0; i < qtde - 1; i++)
  {
    scanf("%d", &pecas[i]);
  }

  printf("Resultados:\n");
  printf("Quantidade: %d\n", qtde);

  for (int i = 0; i < qtde - 1; i++)
    printf("%d", pecas[i]);

  return 0;
}