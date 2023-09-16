/*
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
*/

class Solution {
public:
    int reverse(int x) {
        int initX {x};
        long revX {0};
        while (initX) {
            revX *= 10;
            revX += initX % 10;
            initX /= 10;
        }
        if (revX < std::pow(-2, 31) || revX > std::pow(2, 31) - 1) {
            return 0;
        }
        return revX;
    }
};