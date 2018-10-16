"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
"""

def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    index = 0
    isAny = False
    for char in p:
        if char == '*':
            isAny = True
        elif char == '?':
            isAny = False
            index += 1
            if index == len(s): return True
        else:
            if not isAny:
                if index >= len(s): return False
                elif s[index] == char:
                    index += 1
                    if(index == len(s)):
                        return True
                else:
                    return False
            else:
                for isAnyIndex in range(index, len(s)):
                    if s[isAnyIndex] == char:
                        index = isAnyIndex + 1
                        isAny = False
                        break
                if isAny:
                    return True
    if index >= len(s) or isAny:
        return True
    return False

print(isMatch("aa", "a"))
print(isMatch("aa", "*"))
print(isMatch("cb", "?a"))
print(isMatch("acdeb", "a*b"))
print(isMatch("acdcb", "a*c?b"))
