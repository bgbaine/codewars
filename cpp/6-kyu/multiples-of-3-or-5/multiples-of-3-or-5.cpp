int solution(int number)
{
  int s = 0;
  int n = number - 1;
  while (n > 0)
  {
    if (n % 5 == 0)
    {
      s += n;
      n--;
      continue;
    }
    if (n % 3 == 0)
    {
      s += n;
    }
    n--;
  }
  return s;
}