def repeatedSubstringPattern(s):
    string = (s + s)[1:-1]
    return string.find(s) != -1

print(repeatedSubstringPattern("abcabcabcabc"))
