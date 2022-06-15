def ispalidrome(s):
    return s == s[::-1]
s = 'tamil'
ans = ispalidrome(s)
if ans:
    print("palidrome")
else:
    print(" not palidrome") 