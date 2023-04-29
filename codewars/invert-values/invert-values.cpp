/*
Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.
*/

#include <vector>

std::vector<int> invert(std::vector<int> values)
{
    for (int i = 0; i < (values.size()); ++i) {
        values[i] *= -1;
    }
    return values;
}