"""
- Result -
Runtime: 36 ms, faster than 43.71% of Python3 online submissions for Reverse Integer.
Memory Usage: 14.1 MB, less than 75.49% of Python3 online submissions for Reverse Integer.
"""
class Solution:
    MAX_VALUE = 2147483647
    MIN_VALUE = -2147483648
    def reverse(self, x: int) -> int:
        if x < 0:
            sign_flag = True
            x = -x
        else:
            sign_flag = False

        digit2str = str(x)
        char_list = [elem for elem in digit2str]
        char_list.reverse()

        out = ''
        for elem in char_list:
            out += elem

        out = int(out) if not sign_flag else -int(out)
        out = 0 if out > self.MAX_VALUE or out < self.MIN_VALUE else out

        return out

if __name__ == "__main__":
    inp = 0
    sol = Solution()
    out = sol.reverse(inp)
    print(out)