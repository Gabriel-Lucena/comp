#include <stdio.h>

int main()
{
  int horas;
  float velocidadeMedia;

  scanf("%d", &horas);

  scanf("%f", &velocidadeMedia);

  printf("%.3f", horas * velocidadeMedia / 12);

  printf("\n");

  return 0;
}