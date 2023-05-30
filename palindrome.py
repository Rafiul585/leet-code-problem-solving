x = 123431

class Solution:
    # Way 1 ----------->
    def isPalindrome(self, x: int) -> bool:
        y = ""
        x = str(x)
        length = (len(x)) - 1
    
        for i in range(length, -1, -1):
            y = y + x[i]

        if x == y:
            return True
        else:
            return False
        
    def isPalindrome2(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
        
    # Way 3 ----------->
    def isPalindrome3(self, x):
        
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        half = 0
        while x > half:
            half = (half * 10) + (x % 10)
            x = x // 10
        return x == half or x == half // 10



solution = Solution()
result = solution.isPalindrome3(x)
print(result)

