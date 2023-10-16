s = input('enter str: ')

print(s[2])
print(s[-2])
print(s[0:5])
print(s[0:-2])

result = ''
result2 = ''
for i in range(len(s)):
    if i % 2 == 0:
        result += s[i]
    else:
        result2 += s[i]

print(result)
print(result2)
print(s[::-1])
print(s[::-2])
print(len(s))
