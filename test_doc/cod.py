s = input()
cnt = 1
output = s[0]
if len(s) == 1:
    output = output + str(cnt)

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        cnt += 1
        if i == len(s) - 1:
            output = output + str(cnt)
    else:
        output = output + str(cnt) + s[i]
        cnt = 1
        if i == len(s) - 1:
            output = output + str(cnt)

print(output)