/*
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
*/

class Solution {
public:
    string multiply(string num1, string num2) {
        double numericNum1 = stod(num1.c_str());
        double numericNum2 = stod(num2.c_str());
        long mult = numericNum1 * numericNum2;
        string sMult = to_string(mult);
        return sMult;
    }
};