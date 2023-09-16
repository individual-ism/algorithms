// Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution {
public:
    bool isPalindrome(int x) {
        long revX {0};
        int initX {x};
        while (initX) {
            revX *= 10;
            revX += initX % 10;
            initX /= 10;
        }
        std::cout << revX;
        if (x == revX && x >= 0) {
            return true;
        }
        return false;
    }
};