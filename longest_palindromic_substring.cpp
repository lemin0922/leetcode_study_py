#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
using namespace std;

bool check[1000][1000];
bool P[1000][1000];

bool findPalindrome(string s, int i, int j) {
	if (check[i][j]) return P[i][j];

	check[i][j] = true;
	if (i == j) return true;
	else if (i + 1 == j) {
		if (s[i] == s[j]) return true;
		else return false;
	}
	else {
		P[i + 1][j - 1] = findPalindrome(s, i + 1, j - 1);
		if (P[i + 1][j - 1] && s[i] == s[j]) return true;
		else return false;
	}
}

int main() {
	int max_length = -1;
	int l_idx, r_idx;
	l_idx = 0;
	r_idx = 0;
	string s = "ababa";
	int length = s.length();
	string output;

	memset(check, false, sizeof(check));
	memset(P, false, sizeof(P));

	for (int i = 0; i < length; i++) {
		for (int j = 0; j < length; j++) {
			if (i <= j) {
				P[i][j] = findPalindrome(s, i, j);
				if (P[i][j]) {
					if (max_length < j - i + 1) {
						max_length = j - i + 1;
						l_idx = i;
						r_idx = j;
					}
				}
			}
		}
	}

	cout << s.substr(l_idx, max_length) << endl;

	return 0;
}