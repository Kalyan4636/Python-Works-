# whether string is palindrome or not

s = "nitin"
if s == s[::-1]:
    print("Yes Palindrome")
else:
    print("No")


#Alternative Way
s = "nitsin"
n = len(S)
x = 0
for i in range(n):
    if s[i] != s[n-i-1]:
        x = 1
        break

if x ==0:
    print("Yes Palindrome")
else:
    print("No")

    
