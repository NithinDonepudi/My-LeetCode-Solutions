class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        prev=0
        num=0
        for i in range(len(s)):
            num=num+values[s[i]]
            if prev<values[s[i]]:
                num=num-2*prev
            prev=values[s[i]]
        return num