int maxMultiple(int divisor, int bound) 
{
  // Your Code is Here ... Enjoy !!! 
  while (bound % divisor != 0) {
    bound--;
  }
  return bound;
}