#include <stdio.h>

int main()
{
  float salario, imposto;

  scanf("%f", &salario);

  if (salario <= 2000)
  {
    printf("Isento");
  }
  else
  {
    if (salario <= 3000)
    {
      imposto = (salario - 2000) * .08;
    }
    else if (salario <= 4500)
    {
      imposto = (salario - 3000) * .18 + 1000 * .08;
    }
    else
    {
      imposto = (salario - 4500) * .28 + 1500 * .18 + 1000 * .08;
    }

    printf("R$ %.2f", imposto);
  }

  printf("\n");

  return 0;
}