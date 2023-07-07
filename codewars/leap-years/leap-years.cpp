bool IsLeapYear(int year) 
{
  if (year % 400 == 0) {
    return true;
  } else if (year % 100 == 0) {
    return false;
  } else if (year % 4 == 0) {
    return true;
  } else {
    return false;
  }
}

// Sample Tests
bool IsLeapYear(int year);

Describe(BasicTests)
{
  It(Year_2020_is_a_leap_year) {
      Assert::That(IsLeapYear(2020), Equals(true));
  }

  It(Year_2000_is_a_leap_year) {
      Assert::That(IsLeapYear(2000), Equals(true));
  }

  It(Year_2015_is_not_a_leap_year) {
      Assert::That(IsLeapYear(2015), Equals(false));
  }

  It(Year_2100_is_not_a_leap_year) {
      Assert::That(IsLeapYear(2100), Equals(false));
  }
};