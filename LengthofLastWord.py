class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()

        words = s.split()

        if len(words) == 0:
            return 0

        last_word = words[-1]
        return len(last_word)
