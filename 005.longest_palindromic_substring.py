# Link: https://leetcode.com/problems/longest-palindromic-substring/

## my trial
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         outputs = []
#         candidates = []
#         pairs = []
#         max_length = -1
#
#         length = len(s)
#         for i in range(length):
#             char = s[i]
#             remained = s[i + 1:]
#
#             indices = [idx + i + 1 for idx, elem in enumerate(remained) if elem == char if i + 2 >= idx + i + 1]
#             for j in range(len(indices)):
#                 end_idx = indices[j]
#                 candid = s[i:end_idx + 1]
#
#                 candid_length = len(candid)
#                 second_half = ''
#                 idx = -1
#                 if candid_length % 2 == 0:  # even
#                     half_idx = candid_length // 2
#                     first_half = candid[:half_idx]
#                     _second_half = candid[half_idx:]
#
#                     for k in range(len(_second_half)):
#                         second_half += _second_half[idx]
#                         idx -= 1
#
#                     if first_half == second_half:
#                         if max_length <= len(candid):
#                             candidates.append(candid)
#                             pairs.append((i, end_idx))
#                             max_idx = len(pairs) - 1
#                             max_length = len(candid)
#
#                 else:  # odd
#                     half_idx = candid_length // 2
#                     first_half = candid[:half_idx]
#                     _second_half = candid[half_idx + 1:]
#
#                     for k in range(len(_second_half)):
#                         second_half += _second_half[idx]
#                         idx -= 1
#
#                     if first_half == second_half:
#                         if max_length <= len(candid):
#                             candidates.append(candid)
#                             pairs.append((i, end_idx))
#                             max_length = len(candid)
#                             max_idx = len(pairs) - 1
#
#         if len(candidates) == 0:
#             output = s[0]
#         else:
#             for pair in pairs:
#                 start, end = pair
#
#                 while True:
#                     start -= 1
#                     end += 1
#
#                     if start < 0 and end >= length:
#                         break
#
#                     start = start if start >= 0 else 0
#                     end = end if end < length else length - 1
#
#                     if s[start] == s[end]:
#                         res = s[start:end+1]
#
#                         # check
#                         l_idx = 1
#                         r_idx = -2
#                         flag = False
#                         for _ in range(1, len(res) // 2):
#                             if res[l_idx] == res[r_idx]:
#                                 l_idx += 1
#                                 r_idx -= 1
#                             else:
#                                 flag = True
#                                 break
#
#                         if not flag:
#                             if max_length <= len(res):
#                                 outputs.append(res)
#
#                 # res = s[start:end+1]
#                 # if candid != res:
#                 #     if max_length <= len(res):
#                 #         outputs.append(res)
#
#             if len(outputs) == 0:
#                 output = candidates[max_idx]
#             else:
#                 output = outputs[-1]
#
#         return output

# solution
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
            list_[i] = max(count1,count2)
        max_ = index = 0
        for j in range(len(list_)):
            if max_ < list_[j]:
                max_ = list_[j]
                index = j
        if max_ % 2 == 0:
            return s[index - max_ // 2 + 1:index + 1 + max_ // 2]
        else:
            return s[index - (max_ + 1) // 2 + 1:index + (max_ + 1) // 2]

if __name__ == "__main__":
    inp = "aacabdkacaa"
    sol = Solution()
    output = sol.longestPalindrome(inp)
    print(output)