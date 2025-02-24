#3. Longest Substring Without Repeating Characters

class Solution(object):
    def lengthOfLongestSubstring(self,s):
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            # If the current character is already in the set, move the left pointer
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            # Add the current character to the set
            char_set.add(s[right])
            # Update the maximum length
            max_length = max(max_length, right - left + 1)

        return max_length