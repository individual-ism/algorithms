/*
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
*/

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        std::vector<int>::iterator exists = std::find(nums.begin(), nums.end(), target);
        if (exists != nums.end()) {
            return (std::distance(nums.begin(), exists));
        } else {
            int i = 0;
            while (i < nums.size() && nums[i] < target) {
                i++;
            };
            return i;
        }
    }
};