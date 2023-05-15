#include <stdio.h>
#include <math.h>

int main()
{
  double dx = 0.0000001, area = 0, y, x_0 = 0, x = 1;

  printf("Digite o limite inicial: ");
  scanf("%lf", &x_0);

  printf("Digite o limite final: ");
  scanf("%lf", &x);

  while (x_0 < x)
  {
    y = x_0 + dx; // y = f(x + dx)
    area += y * dx;
    x_0 += dx;
  }

  printf("Area = %g", area);

  return 0;
}