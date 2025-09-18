s = str(input())
x = len(s)
i = 0
x = x - 1
k = 0
while x - i >= i:
    if s[x - i] == s[i]:
        i += 1
    else:
        k = 1
        break
if k == 1:
  print("no")
else:
  print("yes")

