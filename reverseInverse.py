def reverseInverse(s):
    t = []
    i = 0
    while (i < len(s) and not s[i].isalpha()) and not s[i].isnumeric():
        i = i + 1
    j = i
    while (j < len(s) and (s[j].isalpha() or s[j].isnumeric())):
        if s[j].isupper():
            t.append(j)
        j = j + 1
    if j == len(s):
        return s[0:j]
    g = s[0:i] + s[i:j][::-1]
    g = g.upper()
    for y in t:
        g = g[:y] + g[y].lower() + g[y + 1:]
    return g+ reverseInverse(s[j:len(s)])

print(reverseInverse("So, what is CodeFights?"))
print(reverseInverse("Hey, What's Up!"))
print(reverseInverse("First question: How do CodeBots work?"))