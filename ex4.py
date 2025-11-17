# 문제 4 — 가장 긴 줄 찾기

f = open("lines.txt", "r", encoding="utf-8")
longest = ""
for line in f:
    if len(line) > len(longest):
        longest = line
f.close()
print(longest.rstrip())
