/*
An array arr a mountain if the following properties hold:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.
*/

// More time efficient; less memory efficient
class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        int i = 0;
        while (arr[i] < arr[i + 1]) {
            i++;
        };
        return i;
    };
};

// Less time efficient; more memory efficient
class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        for (int i = 0; i < arr.size(); i++) {
            if (arr[i] > arr[i + 1]) {
                return i;
            };
            continue;
        };
        return -1;
    };
};