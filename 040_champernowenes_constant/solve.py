a = []
for i in range(1800000):
    a.append(str(i))

s = ''.join(a)

print(int(s[1]) * int(s[10]) * int(s[100]) * int(s[1000]) * int(s[10000]) * int(s[100000]) * int(s[1000000])  )