#include <stdio.h>

int main()
{
  int segundos, segundosConvertidos = 0,
                minutos = 0, horas = 0;

  scanf("%d", &segundos);

  segundosConvertidos = segundos % 60;
  minutos = segundos / 60;

  if (minutos >= 60)
  {
    horas = minutos / 60;
    minutos = minutos % 60;
  }

  printf("%d:%d:%d", horas, minutos, segundosConvertidos);

  printf("\n");

  return 0;
}
