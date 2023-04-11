/* 
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
*/

class Solution {
public:
    int search(vector<int>& nums, int target) {
        std::vector<int>::iterator exists = std::find(nums.begin(), nums.end(), target);
        if (exists != nums.end()) {
            int index = std::distance(nums.begin(), exists);
            return index;
        } else {
            return -1;
        }
    }
};