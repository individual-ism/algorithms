/*
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
*/

class Solution {
public:
    int maxArea(vector<int>& height) {
        int area{std::min(height[0], height[1])};
        for (int i = 0; i < height.size() - 1; i++) {
            for (int j = 2; j < height.size(); j++) {
                if (std::min(height[i], height[j]) * (j - i) > area) {
                    area = std::min(height[i], height[j]) * (j - i);
                }
            }
        }
        return area;
    }
};