function squareSum(numbers) {
  let sum = 0;
  for (const number of numbers) {
    sum += Math.pow(number, 2);
  }
  return sum;
}
