#include <stdio.h>

int main()
{
  int quilometros;
  float litros;

  scanf("%d", &quilometros);

  scanf("%f", &litros);

  printf("%.3f km/l", quilometros / litros);

  printf("\n");

  return 0;
}