// Initial solution
int stray(std::vector<int> numbers) {
  int i{1};
  if (numbers[0] != numbers[1]) {
    if (numbers[0] == numbers[2]) {
      return numbers[1];
    } else {
      return numbers[0];
    }
  }
  while (numbers[i] == numbers[i - 1]) {
    i++;
  };
  return numbers[i];
};