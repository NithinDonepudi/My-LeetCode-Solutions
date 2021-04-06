class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffle=''
        for i in range(len(s)):
            shuffle=shuffle+s[indices.index(i)]
        return shuffle

            