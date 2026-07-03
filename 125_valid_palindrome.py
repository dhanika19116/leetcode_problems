class Solution(object):
    def isPalindrome(self, s):
     l=[]
     for i in s:
        if i.isalnum():
            l.append(i.lower())
     return l==l[::-1]