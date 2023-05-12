#include <stdio.h>

int main()
{
  float numero;

  scanf("%f", &numero);

  if ((numero >= 0) && (numero <= 100))
  {
    if (numero <= 25)
    {
      printf("Intervalo [0,25]");
    }
    else if (numero <= 50)
    {
      printf("Intervalo (25,50]");
    }
    else if (numero <= 75)
    {
      printf("Intervalo (50,75]");
    }
    else
    {
      printf("Intervalo (75,100]");
    }
  }
  else
  {
    printf("Fora de intervalo");
  }

  printf("\n");

  return 0;
}