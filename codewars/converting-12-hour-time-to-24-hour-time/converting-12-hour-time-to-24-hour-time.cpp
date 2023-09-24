#include <string>

std::string to24HourTime(int hour, int minute, const std::string& period) {
  std::string stringifiedMinutes {minute < 10 ? std::to_string(0) + std::to_string(minute) : std::to_string(minute)};
  std::string stringifiedHour {period == "am" ? (hour == 12 ? "00" : (hour > 9 ? std::to_string(hour) : "0" + std::to_string(hour))) : (hour == 12 ? std::to_string(hour) : std::to_string(hour + 12))};
  return stringifiedHour + stringifiedMinutes;
}