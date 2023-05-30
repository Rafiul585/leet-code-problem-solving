x = 1234


class Solution:

    def isPalindrome(self, x: int) -> bool:
        print(str(x)[::-1])
        # y = ""
        # x = str(x)
        # length = (len(x)) - 1
    
        # for i in range(length, -1, -1):
        #     y = y + x[i]

        # if x == y:
        #     return True
        # else:
        #     return False



solution = Solution()
solution.isPalindrome(x)