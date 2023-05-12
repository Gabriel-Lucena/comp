#include <stdio.h>

int main()
{

  int numeroEmpregado, horasTrabalho;
  float hora;

  scanf("%d", &numeroEmpregado);

  scanf("%d", &horasTrabalho);

  scanf("%f", &hora);

  printf("NUMBER = %d\n", numeroEmpregado);
  printf("SALARY = U$ %.2f", horasTrabalho * hora);

  printf("\n");

  return 0;
}