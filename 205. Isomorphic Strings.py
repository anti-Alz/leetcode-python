"""
205. Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.
Given "foo", "bar", return false.
Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if not s and not t:
            return True
        
        if len(s)!=len(t):
            return False
        
        N = len(s)
        stMap, tsMap = dict(), dict()
        
        for i in range(N):
            if not stMap.get(s[i]):
            	stMap[s[i]] = t[i]
            else:
            	if t[i]!=stMap.get(s[i]):
            		return False

            if not tsMap.get(t[i]):
                tsMap[t[i]] = s[i]
            else:
                if s[i]!=tsMap.get(t[i]):
                    return False
            
        return True


"""
"egg"
"add"
"foo"
"bar"
"paper"
"title"
"ab"
"aa"
"""