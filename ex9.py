# 문제 9 — 단어별 등장 횟수 세기

f = open("words.txt", "r")
words = f.read().split()
f.close()

counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

for word, cnt in counts.items():
    print(f"{word}: {cnt}")
