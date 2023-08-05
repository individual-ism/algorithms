/*
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
*/

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string combinedString = "";
        for (int i = 0; i < min(word1.size(), word2.size()); i++) {
            combinedString += word1[i];
            combinedString += + word2[i];
        }
        if (word1.size() == word2.size()) {
            return combinedString;
        }
        for (int i = min(word1.size(), word2.size()); i < max(word1.size(), word2.size()); i++) {
            if (word1.size() > word2.size()) {
                combinedString += word1[i];
            } else {
                combinedString += word2[i];
            }

        }
        return combinedString;
    }
};