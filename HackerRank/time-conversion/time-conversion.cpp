#include <bits/stdc++.h>
#include <iostream>

using namespace std;

/*
 * Complete the 'timeConversion' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

string timeConversion(string s) {
    if (s[8] == 'A') {
        if (s.substr(0, 2) == "12") {
            s.replace(0, 2, "00");
        }
        return s.substr(0, 8);  
    } else {
        if (s.substr(0, 2) != "12") {
            s.replace(0, 2, to_string(stoi(s.substr(0, 2)) + 12)); 
        }
        return s.substr(0, 8);
    }
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = timeConversion(s);

    fout << result << "\n";

    fout.close();

    return 0;
}