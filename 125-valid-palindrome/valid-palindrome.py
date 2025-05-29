class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        text = filter(lambda x: x.isalnum(), lower(s))
        return (text == text[::-1])
        