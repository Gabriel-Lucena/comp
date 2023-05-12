#include <stdio.h>

int main()
{
  char nomeVendedor[50];
  double salarioFixo, totalVendido;

  scanf("%s", &nomeVendedor);

  scanf("%lf", &salarioFixo);

  scanf("%lf", &totalVendido);

  printf("TOTAL = R$ %.2f", salarioFixo + .15 * totalVendido);

  printf("\n");

  return 0;
}