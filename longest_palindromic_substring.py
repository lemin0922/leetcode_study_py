# Link: https://leetcode.com/problems/longest-palindromic-substring/

## [SOLUTION] method of dynamic programming
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_ = [1] * len(s)
        for i in range(len(s)):
            count1 = count2 = 1
            if i + 1 < len(s) and s[i] == s[i+1]:
                mid = 1
                count1 = 2
                while i - mid >= 0 and i + 1 + mid < len(s) and s[i-mid] == s[i+1+mid]:
                    count1 += 2
                    mid += 1
            if i-1 >= 0 and i+1 < len(s) and s[i-1] == s[i+1]:
                mid = 1
                count2 = 1
                while i - mid >= 0 and i + mid < len(s) and s[i-mid] == s[i+mid]:
                    count2 += 2
                    mid += 1
            list_[i] = max(count1, count2)
        max_ = index = 0
        for j in range(len(list_)):
            if max_ < list_[j]:
                max_ = list_[j]
                index = j
        if max_ % 2 == 0:
            return s[index - max_ // 2 + 1:index + 1 + max_ // 2]
        else:
            return s[index - (max_ + 1) // 2 + 1:index + (max_ + 1) // 2]

# my method (refer to solution) --> Time Limit Exceeded
# class Solution:
#     def longestPalindrome(self, s):
#         length = len(s)
#         self.s = s
#         self.P = [[False for _ in range(len(s))] for _ in range(len(s))]
#         self.check = [[False for _ in range(len(s))] for _ in range(len(s))]
#         max_length = -1
#         l_idx = r_idx = 0
#
#         for i in range(length):
#             for j in range(length):
#                 if i <= j:
#                     self.P[i][j] = self.findPalindrome(i, j)
#                     if self.P[i][j]:
#                         if max_length < j - i + 1:
#                             max_length = j - i + 1
#                             l_idx, r_idx = i, j
#
#         return s[l_idx:r_idx+1]
#
#     def findPalindrome(self, i, j):
#         if self.check[i][j]:
#             return self.P[i][j]
#
#         self.check[i][j] = True
#         if i == j:
#             return True
#         elif i + 1 == j:
#             return True if self.s[i] == self.s[j] else False
#         else:
#             self.P[i+1][j-1] = self.findPalindrome(i+1, j-1)
#             self.P[i][j] = True if self.P[i+1][j-1] and self.s[i] == self.s[j] else False
#             return self.P[i][j]

if __name__ == "__main__":
    inp = "ababa"
    sol = Solution()
    output = sol.longestPalindrome(inp)
    print(output)