class Solution:
    def romanToInt(self, s: str) -> int:
        I=1
        V=5
        X=10
        L=50
        C=100
        D=500
        M=1000

        int_value = 0

        for i in s:
            if i == "I":
                int_value = int_value + I

            if i == "V":
                int_value = int_value + V
            
            if i == "X":
                int_value = int_value + X

            if i == "L":
                int_value = int_value + L

            if i == "C":
                int_value = int_value + C
            
            if i == "D":
                int_value = int_value + D

            if i == "M":
                int_value = int_value + M

        print(int_value)




solution = Solution()
solution.romanToInt(s = 'IVMC')